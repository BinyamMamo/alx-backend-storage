#!/usr/bin/env python3
"""
Task 14 - Top students (#advanced)
Write a Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    """
    try:
        pipeline = [
            {
                "$project": {
                    "name": 1,
                    "topics": 1,
                    "averageScore": {
                        "$avg": "$topics.score"
                    }
                }
            },
            {
                "$sort": {
                    "averageScore": -1
                }
            }
        ]

        top_students = list(mongo_collection.aggregate(pipeline))
        return top_students
    except Exception as e:
        return []
