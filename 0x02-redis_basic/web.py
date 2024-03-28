#!/usr/bin/env python3
"""
Task 5. Implementing an expiring web cache and tracker [ #Advanced ]
Implement a get_page function (prototype: def get_page(url: str) -> str:)
"""
import requests
from functools import wraps
from typing import Callable


def track_access_count(func: Callable):
    """
    Decorator to track URL access count
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """
        The wrapper function for caching the output.
        """
        import redis
        cache = redis.Redis()

        cache.incr(f"count:{url}")
        cached_response = cache.get(f"cached:{url}")

        if cached_response:
            return cached_response.decode('utf-8')

        result = func(url)
        cache.setex(f"cached:{url}", 10, result)

        return result

    return wrapper


@track_access_count
def get_page(url: str) -> str:
    """
    Get page content using requests and cache it
    """
    return requests.get(url).text
