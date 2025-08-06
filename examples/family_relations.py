"""
Family relations examples demonstrating binary relations.
"""

from predicate_logic import grandparent_of, parent_of


def family_relations_demo():
    """Demonstrate family relations"""
    print("=== Family Relations Demo ===")

    print("\nFamily tree relationships:")
    print("John -> Alice:", parent_of("John", "Alice"))
    print("John -> Bob:", parent_of("John", "Bob"))
    print("Alice -> Charlie:", parent_of("Alice", "Charlie"))
    print("Bob -> David:", parent_of("Bob", "David"))

    print("\nGrandparent relationships:")
    print(f"John is grandparent of Charlie: {grandparent_of('John', 'Charlie')}")
    print(f"Alice is grandparent of David: {grandparent_of('Alice', 'David')}")
    print(f"John is grandparent of David: {grandparent_of('John', 'David')}")


if __name__ == "__main__":
    family_relations_demo()
