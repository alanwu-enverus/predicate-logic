#!/usr/bin/env python3
"""
Test runner script for the predicate logic library.
"""

import sys
import unittest
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


def run_tests():
    """Discover and run all tests"""
    loader = unittest.TestLoader()
    start_dir = project_root / "tests"
    suite = loader.discover(start_dir, pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
