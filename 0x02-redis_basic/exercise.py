#!/usr/bin/env python3
"""
Task 0 - 4 : Redis basics
"""
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    a system to count how many
    times methods of the Cache class are called.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


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

    def get(self, key: str, fn: callable = None) ->\
            Union[str, bytes, int, float]:
        """
        Gets the value from Redis for the given key.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            value = fn(value)
        return value

    def get_int(self, key: str) -> int:
        """
        Gets the value from Redis for the given key as an integer.
        """
        return self.get(key, int)

    def get_str(self, key: str) -> str:
        """
        Gets the value from Redis for the given key as a string.
        """
        return self.get(key, str)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
         Store data in redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
