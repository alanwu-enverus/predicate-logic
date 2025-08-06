"""
Unit tests for logical operators.
"""

import unittest

from predicate_logic.logical_operators import (
    logical_and,
    logical_iff,
    logical_implies,
    logical_not,
    logical_or,
    logical_xor,
)
from predicate_logic.predicates import is_even, is_positive


class TestLogicalOperators(unittest.TestCase):
    def test_logical_and(self):
        even_and_positive = logical_and(is_even, is_positive)
        self.assertTrue(even_and_positive(2))
        self.assertTrue(even_and_positive(4))
        self.assertFalse(even_and_positive(1))  # odd
        self.assertFalse(even_and_positive(-2))  # negative
        self.assertFalse(even_and_positive(-3))  # both

    def test_logical_or(self):
        even_or_positive = logical_or(is_even, is_positive)
        self.assertTrue(even_or_positive(2))  # both
        self.assertTrue(even_or_positive(1))  # positive only
        self.assertTrue(even_or_positive(-2))  # even only
        self.assertFalse(even_or_positive(-3))  # neither

    def test_logical_not(self):
        not_even = logical_not(is_even)
        self.assertTrue(not_even(1))
        self.assertTrue(not_even(3))
        self.assertFalse(not_even(2))
        self.assertFalse(not_even(4))

    def test_logical_implies(self):
        # If even then positive (not always true, but for testing)
        even_implies_positive = logical_implies(is_even, is_positive)
        self.assertTrue(even_implies_positive(2))  # even and positive
        self.assertTrue(even_implies_positive(1))  # not even (vacuously true)
        self.assertTrue(even_implies_positive(3))  # not even (vacuously true)
        self.assertFalse(even_implies_positive(-2))  # even but not positive

    def test_logical_iff(self):
        # Test with simple predicates
        def p(x):
            return x > 0

        def q(x):
            return x > 0  # same predicate

        iff = logical_iff(p, q)
        self.assertTrue(iff(5))
        self.assertTrue(iff(-5))

    def test_logical_xor(self):
        even_xor_positive = logical_xor(is_even, is_positive)
        self.assertFalse(even_xor_positive(2))  # both true
        self.assertTrue(even_xor_positive(1))  # only positive
        self.assertTrue(even_xor_positive(-2))  # only even
        self.assertFalse(even_xor_positive(-3))  # both false


if __name__ == "__main__":
    unittest.main()
