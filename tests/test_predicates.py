"""
Unit tests for basic predicates.
"""

import unittest

from predicate_logic.predicates import (
    compose_predicates,
    equals,
    greater_than,
    is_even,
    is_positive,
    less_than,
)


class TestBasicPredicates(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))

    def test_is_positive(self):
        self.assertTrue(is_positive(1))
        self.assertTrue(is_positive(100))
        self.assertFalse(is_positive(0))
        self.assertFalse(is_positive(-1))
        self.assertFalse(is_positive(-100))

    def test_greater_than(self):
        gt_5 = greater_than(5)
        self.assertTrue(gt_5(6))
        self.assertTrue(gt_5(10))
        self.assertFalse(gt_5(5))
        self.assertFalse(gt_5(4))
        self.assertFalse(gt_5(-1))

    def test_less_than(self):
        lt_5 = less_than(5)
        self.assertTrue(lt_5(4))
        self.assertTrue(lt_5(-1))
        self.assertFalse(lt_5(5))
        self.assertFalse(lt_5(6))
        self.assertFalse(lt_5(10))

    def test_equals(self):
        eq_5 = equals(5)
        self.assertTrue(eq_5(5))
        self.assertFalse(eq_5(4))
        self.assertFalse(eq_5(6))

    def test_compose_predicates(self):
        even_and_positive = compose_predicates(is_even, is_positive)
        self.assertTrue(even_and_positive(2))
        self.assertTrue(even_and_positive(4))
        self.assertFalse(even_and_positive(1))  # odd
        self.assertFalse(even_and_positive(-2))  # negative


if __name__ == "__main__":
    unittest.main()
