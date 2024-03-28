import unittest
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

    def test_get_page_expires_cache(self):
        url = 'http://example.com'
        get_page(url)
        self.cache.set(f'cached:{url}', 'cached value')
        response = get_page(url)
        self.assertNotEqual(response, 'cached value')

    def test_get_page_increments_count(self):
        url = 'http://example.com'
        count1 = self.cache.get(f'count:{url}')
        get_page(url)
        count2 = self.cache.get(f'count:{url}')
        self.assertEqual(int(count2), int(count1) + 1)
