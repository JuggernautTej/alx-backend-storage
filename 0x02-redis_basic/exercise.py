#!/usr/bin/env python3
"""A script that creates a class called Cache thats stores
an instance of a Redis client and has a method called store
that takes a data argument and returns aa string"""

import redis
import uuid
from typing import Union


class Cache:
    """The cache class"""
    def __init__(self) -> None:
        """This initializes the instance of redis and
        clears the current database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
