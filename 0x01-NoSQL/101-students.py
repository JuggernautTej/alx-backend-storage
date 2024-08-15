#!/usr/bin/env python3
"""A Python script that returns all students sorted by
average score."""


def top_students(mongo_collection):
    """A python function that returns all students sorted by
    the average score.
    Args:
        mongo_collection: A pymongo collection object
    Returns:
        List[dict]: A list of dictionaries representing
        the student documents sorted by their average
        score"""
    # Uses the aggregate method to calculate the average
    # score for each student and sort the results
    students = mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])
    return [student for student in students]
