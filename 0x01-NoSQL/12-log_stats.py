#!/usr/bin/env python3
"""
Task 12 - Log stats
Write a Python script that provides some
stats about Nginx logs stored in MongoDB
"""
def nginx_logs_stats(mongo_collection):
    """
    Provides statistics about Nginx logs stored in a MongoDB collection.
    """
    try:
        total_logs = mongo_collection.count_documents({})

        print(f"{total_logs} logs")

        http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in http_methods:
            count = mongo_collection.count_documents({"method": method})
            print(f"\t{method}: {count}")

        count_status = mongo_collection.count_documents({"method": "GET", "path": "/status"})
        print(f"method=GET path=/status: {count_status}")
    except Exception as e:
        print(f"Error fetching stats: {e}")


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    nginx_logs_stats(collection)
