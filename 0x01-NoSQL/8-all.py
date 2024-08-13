#!/usr/bin/env python3
"""A Python function that lists all documents in a
collection."""


def list_all(mongo_collection):
    """This method lists all documents in a collection.
    Args:
        mongo_collection: a pymongo collection object.
    Returns:
        List: A list of all documents in the collection."""
    d_list = list(mongo_collection.find())
    return d_list
    # client = MongoClient()
    # db = client.my_db
    # school = db.school
    # d_list = school.find()
    # return d_list
