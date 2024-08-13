#!/usr/bin/env python3
"""A Python function that inserts a new document in
a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """This method lists all documents in a collection.
    Args:
        mongo_collection: a pymongo collection object.
    Returns:
        List: A list of all documents in the collection."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
