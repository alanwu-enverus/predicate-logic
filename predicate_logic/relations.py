"""
Binary relations and relation properties.

This module provides functions for working with binary relations
and checking their properties (reflexive, symmetric, transitive, etc.).
"""

from typing import Any, Callable, Iterable, Tuple, TypeVar

from .logical_operators import logical_implies
from .quantifiers import forall

# Type variables
T = TypeVar("T")
U = TypeVar("U")

# Type aliases
BinaryRelation = Callable[[T, T], bool]
Predicate = Callable[[T], bool]


def loves(person1: str, person2: str) -> bool:
    """Binary predicate: person1 loves person2"""
    # This would typically check some data structure
    relationships = {("Alice", "Bob"), ("Bob", "Charlie"), ("Alice", "Alice")}
    return (person1, person2) in relationships


def parent_of(parent: str, child: str) -> bool:
    """Example binary relation: parent-child relationship"""
    family_tree = {
        ("John", "Alice"),
        ("John", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "David"),
    }
    return (parent, child) in family_tree


def grandparent_of(grandparent: str, grandchild: str) -> bool:
    """Derived relation: grandparent if parent of parent"""
    from .quantifiers import exists

    people = ["John", "Alice", "Bob", "Charlie", "David"]
    return exists(
        lambda middle: parent_of(grandparent, middle) and parent_of(middle, grandchild),
        people,
    )


def is_reflexive(relation: BinaryRelation[T], domain: Iterable[T]) -> bool:
    """Check if a binary relation is reflexive"""
    return forall(lambda x: relation(x, x), domain)


def is_symmetric(relation: BinaryRelation[T], domain: Iterable[T]) -> bool:
    """Check if a binary relation is symmetric"""
    return forall(
        lambda x: forall(
            lambda y: logical_implies(
                lambda _: relation(x, y), lambda _: relation(y, x)
            )(None),
            domain,
        ),
        domain,
    )


def is_transitive(relation: BinaryRelation[T], domain: Iterable[T]) -> bool:
    """Check if a binary relation is transitive"""
    return forall(
        lambda x: forall(
            lambda y: forall(
                lambda z: logical_implies(
                    lambda _: relation(x, y) and relation(y, z),
                    lambda _: relation(x, z),
                )(None),
                domain,
            ),
            domain,
        ),
        domain,
    )


def is_equivalence_relation(relation: BinaryRelation[T], domain: Iterable[T]) -> bool:
    """Check if a relation is an equivalence relation"""
    return (
        is_reflexive(relation, domain)
        and is_symmetric(relation, domain)
        and is_transitive(relation, domain)
    )


def cartesian_predicate(
    pred1: Predicate[T], pred2: Predicate[U]
) -> Predicate[Tuple[T, U]]:
    """Create predicate over cartesian product of domains"""

    def cart_pred(xy_pair: Tuple[T, U]) -> bool:
        x, y = xy_pair
        return pred1(x) and pred2(y)

    return cart_pred


def bind_variable(
    predicate: Callable[..., Any], var_index: int, value: Any
) -> Callable[..., Any]:
    """Bind a specific variable in a multi-argument predicate"""

    def bound_predicate(*args: Any) -> Any:
        new_args = list(args)
        new_args.insert(var_index, value)
        return predicate(*new_args)

    return bound_predicate
