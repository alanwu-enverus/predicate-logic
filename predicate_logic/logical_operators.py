"""
Logical operators for predicate logic.

This module implements logical operators as higher-order functions
that can be used to combine predicates.
"""

from typing import Callable, TypeVar

# Type variable for the input type to predicates
T = TypeVar("T")

# Type alias for a predicate function
Predicate = Callable[[T], bool]


def logical_and(pred1: Predicate[T], pred2: Predicate[T]) -> Predicate[T]:
    """Conjunction: P ∧ Q"""
    return lambda x: pred1(x) and pred2(x)


def logical_or(pred1: Predicate[T], pred2: Predicate[T]) -> Predicate[T]:
    """Disjunction: P ∨ Q"""
    return lambda x: pred1(x) or pred2(x)


def logical_not(pred: Predicate[T]) -> Predicate[T]:
    """Negation: ¬P"""
    return lambda x: not pred(x)


def logical_implies(pred1: Predicate[T], pred2: Predicate[T]) -> Predicate[T]:
    """Implication: P → Q (equivalent to ¬P ∨ Q)"""
    return lambda x: (not pred1(x)) or pred2(x)


def logical_iff(pred1: Predicate[T], pred2: Predicate[T]) -> Predicate[T]:
    """Biconditional: P ↔ Q (P if and only if Q)"""
    return lambda x: pred1(x) == pred2(x)


def logical_xor(pred1: Predicate[T], pred2: Predicate[T]) -> Predicate[T]:
    """Exclusive or: P ⊕ Q"""
    return lambda x: pred1(x) != pred2(x)
