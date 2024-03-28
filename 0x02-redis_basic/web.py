#!/usr/bin/env python3
"""
Task 5. Implementing an expiring web cache and tracker [ #Advanced ]
Implement a get_page function (prototype: def get_page(url: str) -> str:)
"""
import requests
import redis
from functools import wraps
from typing import Callable

cache = redis.Redis()


def track_access_count(func: callable):
    """
    Decorator to track URL access count
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """
        The wrapper function for caching the output.
        """

        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")

        if cached_response:
            return cached_response.decode('utf-8')

        result = func(url)
        redis.setex(f"cached:{url}", 10, result)

        return result

    return wrapper


@track_access_count
def get_page(url: str) -> str:
    """
    Get page content using requests and cache it
    """
    return requests.get(url).text
