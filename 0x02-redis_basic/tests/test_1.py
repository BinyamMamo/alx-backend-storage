import unittest
from exercise import get_int

class TestGetInt(unittest.TestCase):

    def test_get_int_valid(self):
        self.assertEqual(get_int('foo', '123'), 123)

    def test_get_int_invalid(self):
        self.assertEqual(get_int('bar', 'abc'), 0)

    def test_get_int_not_found(self):
        self.assertEqual(get_int('baz', None), 0)
