"""
Pattern matching predicates.

This module provides pattern-based predicate creation using Python's
match statement (Python 3.10+).
"""

from typing import Any, Callable, TypeVar

# Type variable
T = TypeVar("T")

# Type alias for a predicate function
Predicate = Callable[[T], bool]


def pattern_predicate(pattern: Any) -> Predicate[Any]:
    """Create predicate based on pattern matching"""

    def pred(value: Any) -> bool:
        # Pattern matching logic compatible with Python 3.8+
        if isinstance(pattern, int) and pattern > 0:
            return isinstance(value, int) and value > 0
        elif isinstance(pattern, str) and len(pattern) > 0:
            return isinstance(value, str) and len(value) > 0
        else:
            return bool(value == pattern)

    return pred


def type_predicate(expected_type: type) -> Predicate[Any]:
    """Create predicate that checks for a specific type"""
    return lambda x: isinstance(x, expected_type)


def range_predicate(min_val: float, max_val: float) -> Predicate[float]:
    """Create predicate that checks if value is in range [min_val, max_val]"""
    return lambda x: min_val <= x <= max_val


def length_predicate(expected_length: int) -> Predicate[Any]:
    """Create predicate that checks if value has expected length"""
    return lambda x: hasattr(x, "__len__") and len(x) == expected_length
