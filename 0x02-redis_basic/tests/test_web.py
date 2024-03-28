import unittest
from unittest.mock import patch
from web import get_page
import redis

class TestGetPage(unittest.TestCase):

    def setUp(self):
        self.cache = redis.Redis()

    def test_get_page_caches_response(self):
        url = 'http://example.com'
        response1 = get_page(url)
        response2 = get_page(url)
        self.assertEqual(response1, response2)

    @patch('web.requests.get')
    def test_get_page_expires_cache(self, mock_get):
        # Mocking the requests.get method to avoid actual HTTP requests
        mock_get.return_value.text = "Mocked page content"
        url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://example.com"

        # First call should make a real request
        result = get_page(url)
        self.assertEqual(result, "Mocked page content")

        # Second call should retrieve from cache
        result = get_page(url)
        self.assertEqual(result, "Mocked page content")

    def test_get_page_increments_count(self):
        url = 'http://example.com'
        count1 = self.cache.get(f'count:{url}')
        get_page(url)
        count2 = self.cache.get(f'count:{url}')
        self.assertEqual(int(count2), int(count1) + 1)
