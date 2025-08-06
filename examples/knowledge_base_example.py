"""
Knowledge base examples demonstrating the PredicateLogic class.
"""

from predicate_logic import PredicateLogic


def knowledge_base_demo():
    """Demonstrate knowledge base functionality"""
    print("=== Knowledge Base Demo ===")

    # Create knowledge base
    kb = PredicateLogic()

    # Add facts
    kb.add_fact(("human", ("socrates",)))
    kb.add_fact(("human", ("plato",)))
    kb.add_fact(("philosopher", ("socrates",)))
    kb.add_fact(("philosopher", ("plato",)))

    # Query facts
    print(f"Socrates is human: {kb.query('human', 'socrates')}")
    print(f"Plato is human: {kb.query('human', 'plato')}")
    print(f"Aristotle is human: {kb.query('human', 'aristotle')}")

    print(f"Socrates is philosopher: {kb.query('philosopher', 'socrates')}")

    print(f"\nAll facts: {kb.get_all_facts()}")


if __name__ == "__main__":
    knowledge_base_demo()
