#!/usr/bin/env python3
"""
Task 15 - Log stats - new version (#advanced)
Improve 12-log_stats.py by adding the top 10 of the most
present IPs in the collection nginx of the database logs
"""


def top_ips(mongo_collection):
    """
    Returns the top 10 most present IPs in the MongoDB collection.
    """
    try:
        pipeline = [
            {
                "$group": {
                    "_id": "$ip",
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "count": -1
                }
            },
            {
                "$limit": 10
            }
        ]

        top_ips = list(mongo_collection.aggregate(pipeline))
        return top_ips
    except Exception as e:
        return []


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    top_ips_list = top_ips(collection)
    for ip in top_ips_list:
        print(f"{ip['_id']}: {ip['count']}")
