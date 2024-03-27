#!/usr/bin/env python3
"""
Task 0 - 4 : Redis basics
"""
import uuid
from typing import Union


class Cache:
    """
    implements the cache
    """

    def __init__(self) -> None:
        """
         Initialize the Redis instance. This is called by __init__
        """
        import redis
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def get(self, key: str, fn: callable) -> Union[str, bytes, int, float]:
        """
        Gets the value from Redis for the given key.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            value = fn(value)
        return value

    def get_int(self, key: str) -> int:
        """
        Gets the value from Redis for the given key as an integer.
        """
        return self.get(key, lambda d: int(d))

    def get_str(self, key: str) -> str:
        """
        Gets the value from Redis for the given key as a string.
        """
        return self.get(key, lambda d: str(d))

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
         Store data in redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
