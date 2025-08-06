"""
Knowledge base for predicate logic.

This module provides a class-based approach for managing facts and rules
in a simple knowledge base system.
"""

from typing import Callable, List, Set, Tuple


class PredicateLogic:
    """Class-based approach for more complex predicate logic"""

    def __init__(self) -> None:
        self.facts: Set[Tuple[str, Tuple[str, ...]]] = set()
        self.rules: List[Tuple[Callable, Tuple[str, Tuple[str, ...]]]] = []

    def add_fact(self, fact: Tuple[str, Tuple[str, ...]]) -> None:
        """Add a ground fact"""
        self.facts.add(fact)

    def add_rule(
        self, condition: Callable, conclusion: Tuple[str, Tuple[str, ...]]
    ) -> None:
        """Add a rule: if condition then conclusion"""
        self.rules.append((condition, conclusion))

    def query(self, predicate: str, *args: str) -> bool:
        """Query if a predicate holds"""
        fact = (predicate, args)

        # Check direct facts
        if fact in self.facts:
            return True

        # Check rules
        for condition, conclusion in self.rules:
            if conclusion == fact and condition(*args):
                return True

        return False

    def get_all_facts(self) -> Set[Tuple[str, Tuple[str, ...]]]:
        """Return all facts in the knowledge base"""
        return self.facts.copy()

    def get_all_rules(self) -> List[Tuple[Callable, Tuple[str, Tuple[str, ...]]]]:
        """Return all rules in the knowledge base"""
        return self.rules.copy()

    def clear(self) -> None:
        """Clear all facts and rules"""
        self.facts.clear()
        self.rules.clear()
