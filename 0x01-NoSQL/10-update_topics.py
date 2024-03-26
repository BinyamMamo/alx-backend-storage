#!/usr/bin/env python3
"""
Task 10 - Change school topics
Write a Python function that changes all
topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
     Update topics for a user
    """
    try:
        query = {"name": name}
        doc = mongo_collection.find_one(query)

        if doc:
            update = {"$set": {"topics": topics}}
            mongo_collection.update_one(query, update)
            return str(doc["_id"])
        else:
            return None
    except Exception:
        return None
