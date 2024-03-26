"""
Task 8 - List all documents in Python
Write a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
     List all documents in a mongo collection
    """
    try:
       return list(mongo_collection.find({}))
    except Exception:
        return []
