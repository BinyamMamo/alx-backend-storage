#!/usr/bin/env python3
"""
Task 9 - Insert a document in Python
Write a Python function that inserts a new
document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
     Insert a school into a mongo collection
    """
    try:
        result = mongo_collection.insert_one(kwargs)
        return result.inserted_id
    except Exception:
        return None
