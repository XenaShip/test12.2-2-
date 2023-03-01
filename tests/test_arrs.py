import unittest
from utils.arrs import get
from utils.arrs import my_slice


class TestGet(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([], 0, "test"), "test")
        self.assertEqual(get([3, 48, 5], -10), None)
        self.assertEqual(get([1, 2, 3, 4], 10), None)


class TestMySlice(unittest.TestCase):
    def test_my_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4], -1, 3), [])
        self.assertEqual(my_slice([1, 2, 3, 3], -1, 1), [])
        self.assertEqual(my_slice([1, 2], 1, 4), [2])
        self.assertEqual(my_slice([1, 2, 3, 4], 1, -5), [])
        self.assertEqual(my_slice([1, 2, 3, 4], 0, -1), [1, 2, 3])
        self.assertEqual(my_slice([], 1, 2), [])
        self.assertEqual(my_slice([1, 2, 3, 4], -10, 1), [1])


if __name__ == '__main__':
    unittest.main()


