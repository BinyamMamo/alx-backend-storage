import unittest
from exercise import Cache, replay

class TestCache(unittest.TestCase):

    def setUp(self):
        self.cache = Cache()

    def test_store_valid(self):
        key = self.cache.store('hello')
        self.assertIsInstance(key, str)

    def test_store_bytes(self):
        key = self.cache.store(b'world')
        self.assertIsInstance(key, str)

    def test_store_int(self):
        key = self.cache.store(123)
        self.assertIsInstance(key, str)

    def test_store_float(self):
        key = self.cache.store(1.23)
        self.assertIsInstance(key, str)

    def test_replay_missing_cache(self):
        replay(self.cache.get)

    def test_replay_missing_method(self):
        replay(None)

