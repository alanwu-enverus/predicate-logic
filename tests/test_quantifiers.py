"""
Unit tests for quantifiers.
"""

import unittest

from predicate_logic.predicates import is_even, is_positive
from predicate_logic.quantifiers import (
    count_where,
    exists,
    exists_unique,
    find_all,
    find_first,
    forall,
)


class TestQuantifiers(unittest.TestCase):
    def setUp(self):
        self.positive_numbers = [1, 2, 3, 4, 5]
        self.mixed_numbers = [-2, -1, 0, 1, 2]
        self.even_numbers = [2, 4, 6, 8]

    def test_forall(self):
        self.assertTrue(forall(is_positive, self.positive_numbers))
        self.assertFalse(forall(is_positive, self.mixed_numbers))
        self.assertTrue(forall(is_even, self.even_numbers))

    def test_exists(self):
        self.assertTrue(exists(is_even, self.mixed_numbers))
        self.assertTrue(exists(is_positive, self.mixed_numbers))
        self.assertFalse(exists(is_even, [1, 3, 5]))

    def test_exists_unique(self):
        self.assertTrue(exists_unique(lambda x: x == 0, self.mixed_numbers))
        self.assertFalse(
            exists_unique(is_positive, self.mixed_numbers)
        )  # more than one
        self.assertFalse(exists_unique(lambda x: x == 10, self.mixed_numbers))  # none

    def test_count_where(self):
        self.assertEqual(count_where(is_positive, self.mixed_numbers), 2)
        self.assertEqual(count_where(is_even, self.mixed_numbers), 3)  # -2, 0, 2
        self.assertEqual(count_where(lambda x: x > 10, self.mixed_numbers), 0)

    def test_find_all(self):
        positive_found = find_all(is_positive, self.mixed_numbers)
        self.assertEqual(positive_found, [1, 2])

        even_found = find_all(is_even, self.mixed_numbers)
        self.assertEqual(even_found, [-2, 0, 2])

    def test_find_first(self):
        first_positive = find_first(is_positive, self.mixed_numbers)
        self.assertEqual(first_positive, 1)

        first_large = find_first(lambda x: x > 10, self.mixed_numbers)
        self.assertIsNone(first_large)


if __name__ == "__main__":
    unittest.main()
