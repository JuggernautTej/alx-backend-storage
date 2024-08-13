#!/usr/bin/env python3
"""A Python function that returns the list of school
having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """This method returns the list of school having a specific topic.
    Args:
        mongo_collection: a pymongo collection object.
        topics: a strings of the topic to be searched.
    Returns:
        List: a list of the school."""
    result = mongo_collection.find({"topics": topic})
    return list(result)
