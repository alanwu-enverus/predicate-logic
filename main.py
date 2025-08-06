"""
Main demonstration script for the predicate logic library.

This script runs all the examples to showcase the library functionality.
"""

import sys
from pathlib import Path


def main():
    """Run all demos"""
    # Add the project root to the path so we can import our modules
    project_root = Path(__file__).parent
    sys.path.insert(0, str(project_root))

    # Import demo functions after path setup
    from examples.basic_examples import basic_predicates_demo
    from examples.family_relations import family_relations_demo
    from examples.knowledge_base_example import knowledge_base_demo

    print("Predicate Logic Library Demonstration")
    print("=" * 50)

    try:
        basic_predicates_demo()
        print("\n" + "=" * 50)

        family_relations_demo()
        print("\n" + "=" * 50)

        knowledge_base_demo()
        print("\n" + "=" * 50)

        print("All demos completed successfully!")

    except Exception as e:
        print(f"Error running demos: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
