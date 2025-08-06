"""
Quantifiers for first-order logic.

This module implements universal and existential quantifiers
using functional programming approaches.
"""

from typing import Callable, Iterable, List, Optional, TypeVar

# Type variable for the input type to predicates
T = TypeVar("T")

# Type alias for a predicate function
Predicate = Callable[[T], bool]


def forall(predicate: Predicate[T], domain: Iterable[T]) -> bool:
    """Universal quantifier: ∀x ∈ domain, P(x)"""
    return all(predicate(x) for x in domain)


def exists(predicate: Predicate[T], domain: Iterable[T]) -> bool:
    """Existential quantifier: ∃x ∈ domain, P(x)"""
    return any(predicate(x) for x in domain)


def exists_unique(predicate: Predicate[T], domain: Iterable[T]) -> bool:
    """Unique existence: ∃!x ∈ domain, P(x)"""
    return sum(1 for x in domain if predicate(x)) == 1


def count_where(predicate: Predicate[T], domain: Iterable[T]) -> int:
    """Count how many elements in domain satisfy the predicate"""
    return sum(1 for x in domain if predicate(x))


def find_all(predicate: Predicate[T], domain: Iterable[T]) -> List[T]:
    """Find all elements in domain that satisfy the predicate"""
    return [x for x in domain if predicate(x)]


def find_first(predicate: Predicate[T], domain: Iterable[T]) -> Optional[T]:
    """Find the first element in domain that satisfies the predicate"""
    for x in domain:
        if predicate(x):
            return x
    return None
