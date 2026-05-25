import unittest
from main import bubble_sort, binary_insertion_sort


class TestSortingAlgorithms(unittest.TestCase):

    def test_bubble_sort_normal(self):
        self.assertEqual(bubble_sort([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])

    def test_bubble_sort_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_binary_sort_normal(self):
        self.assertEqual(binary_insertion_sort([8, 2, 7, 3]), [2, 3, 7, 8])

    def test_binary_sort_sorted(self):
        self.assertEqual(binary_insertion_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_binary_sort_negative(self):
        self.assertEqual(binary_insertion_sort([-5, 0, -10, 5]), [-10, -5, 0, 5])


if __name__ == '__main__':
    unittest.main()
