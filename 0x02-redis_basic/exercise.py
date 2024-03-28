#!/usr/bin/env python3
"""
Task 0 - 4 : Redis basics
"""
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A system to count how many times methods of the Cache class are called.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> None:
        """
        Wrapper decorator that counts calls to Cache methods.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorates a Cache method to track call history.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> None:
        """
        Tracks call inputs and outputs.
        """
        key_inputs = "{}:inputs".format(method.__qualname__)
        key_outputs = "{}:outputs".format(method.__qualname__)

        input_str = str(args)
        self._redis.rpush(key_inputs, input_str)

        result = method(self, *args, **kwargs)

        self._redis.rpush(key_outputs, result)

        return result

    return wrapper


def replay(method: Callable) -> None:
    """
    Replays the call history for a method.
    """

    if method is None or not hasattr(method, '__self__'):
        return

    import redis
    cache = getattr(method.__self__, '_redis', None)
    if not isinstance(cache, redis.Redis):
        return

    key_inputs = "{}:inputs".format(method.__qualname__)
    key_outputs = "{}:outputs".format(method.__qualname__)
    inputs = cache.lrange(key_inputs, 0, -1)
    outputs = cache.lrange(key_outputs, 0, -1)

    print("{} was called {} times:".format(method.__qualname__, len(inputs)))
    for inp, outp in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method.__qualname__,
                                     inp.decode("utf-8"),
                                     outp.decode("utf-8")))


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

    def get(self, key: str, fn: Callable = None) ->\
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
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
         Store data in redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
