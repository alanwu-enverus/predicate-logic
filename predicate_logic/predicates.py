"""
Basic predicate functions and utilities.

This module contains fundamental predicate functions and higher-order
functions for creating predicates.
"""

from typing import Callable, TypeVar

# Type variable for the input type to predicates
T = TypeVar("T")

# Type alias for a predicate function
Predicate = Callable[[T], bool]


def is_even(x: int) -> bool:
    """Predicate: x is even"""
    return x % 2 == 0


def is_positive(x: float) -> bool:
    """Predicate: x is positive"""
    return x > 0


def greater_than(threshold: float) -> Predicate[float]:
    """Higher-order predicate: returns a predicate function"""
    return lambda x: x > threshold


def less_than(threshold: float) -> Predicate[float]:
    """Higher-order predicate: returns a predicate function"""
    return lambda x: x < threshold


def equals(value: T) -> Predicate[T]:
    """Higher-order predicate: returns a predicate function for equality"""
    return lambda x: x == value


def compose_predicates(*predicates: Predicate[T]) -> Predicate[T]:
    """Compose multiple predicates with AND logic"""

    def composed_predicate(x: T) -> bool:
        return all(pred(x) for pred in predicates)

    return composed_predicate
