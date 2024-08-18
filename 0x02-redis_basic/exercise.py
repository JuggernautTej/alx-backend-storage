#!/usr/bin/env python3
"""A script that creates a class called Cache thats stores
an instance of a Redis client and has a method called store
that takes a data argument and returns aa string"""

import redis
import uuid
from functools import wraps
from typing import Callable, cast, Optional, TypeVar, Union

T = TypeVar('T', str, bytes, int, float)


def count_calls(method: Callable) -> Callable:
    """A decorator that counts the number of times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """A wrapper function that increments the call count."""
        # Key generation happens using the qualified name of the method
        key = f"{method.__qualname__}:calls"

        # Now the counter for the key is incremented
        self._redis.incr(key)

        # # Store the call count as a string in Redis for easy retrieval
        # self._redis.set(key, call_count)

        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """The cache class"""
    def __init__(self) -> None:
        """This initializes the instance of redis and
        clears the current database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """A method that takes a data argument and returns
        a string.
        Args:
            data: This is either an int, float, string or
            bytes type
        Returns:
            A randomly generated key as a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], T]] = None) -> Optional[T]:
        """A method that takes a key string argument and an optional Callable
        argument named fn.
        Args:
            key: a string.
            fn: The optional callable function.
        Return:
            bytes."""
        data = self._redis.get(key)
        if data is None:
            return None
        # assert isinstance(data, bytes)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """A method that automatically parametrize Cache.get and returns
        a string.
        Args:
            key: a string.
        Return:
            a string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """A method that automatically parametrize Cache.get and returns
        a integer.
        Args:
            key: a string.
        Return:
            an integer."""
        return self.get(key, fn=int)
