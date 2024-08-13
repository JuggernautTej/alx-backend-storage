#!/usr/bin/env python3
"""A Python function that changes all topics of a
school document based on the name."""


def update_topics(mongo_collection, name, topics):
    """This method changes all topics of a school document.
    Args:
        mongo_collection: a pymongo collection object.
        name: a string.
        topics: a list of strings with the topics approached
        in school.
    Returns:
        None."""
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})
