#!/usr/bin/env python3
"""
Task 11 - Where can I learn Python?
Write a Python function that returns the list of school having a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """
     Get schools by topic.
    """
    try:
        query = {"topics": topic}
        schools = list(mongo_collection.find(query))

        return schools
    except Exception:
        return []
