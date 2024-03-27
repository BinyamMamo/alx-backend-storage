#!/usr/bin/env python3
"""
Task 0. Writing strings to Redis
Create a Cache class, initialize _redis, flush it,
and create a store method that accepts data, generates
a key, stores data, and returns the key.
"""
from redis import Redis
import uuid


class Cache():
    """
    implements the cache
    """
    def __init__(self):
        """
         Initialize the Redis instance. This is called by __init__
        """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data):
        """
         Store data in redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
