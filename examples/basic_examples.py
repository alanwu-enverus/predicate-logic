"""
Basic examples demonstrating predicate logic functionality.
"""

from predicate_logic import (
    exists,
    exists_unique,
    forall,
    greater_than,
    is_even,
    is_positive,
    logical_and,
    logical_not,
)


def basic_predicates_demo():
    """Demonstrate basic predicate usage"""
    print("=== Basic Predicates Demo ===")

    # Create compound predicates
    is_even_and_positive = logical_and(is_even, is_positive)
    is_odd = logical_not(is_even)
    greater_than_5 = greater_than(5)

    # Test predicates
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Even and positive numbers:")
    print([n for n in numbers if is_even_and_positive(n)])

    print("\nOdd numbers:")
    print([n for n in numbers if is_odd(n)])

    print("\nNumbers greater than 5:")
    print([n for n in numbers if greater_than_5(n)])

    # Using quantifiers
    print(f"\nAll numbers are positive: {forall(is_positive, numbers)}")
    print(f"Some numbers are even: {exists(is_even, numbers)}")
    print(f"Exactly one number equals 5: {exists_unique(lambda x: x == 5, numbers)}")


if __name__ == "__main__":
    basic_predicates_demo()
