#!/usr/bin/env python3
"""
Run all quality checks for the predicate logic library.
"""

import subprocess
import sys
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent


def run_command(cmd: list[str], description: str) -> bool:
    """Run a command and return whether it succeeded."""
    print(f"\n🔧 {description}")
    print(f"Running: {' '.join(cmd)}")
    print("-" * 50)

    try:
        subprocess.run(cmd, check=True, cwd=project_root)
        print(f"✅ {description} - PASSED")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED (exit code {e.returncode})")
        return False


def main():
    """Run all quality checks."""
    print("🚀 Running all quality checks for predicate-logic library")
    print("=" * 60)

    checks = [
        (["uv", "run", "pytest", "tests/", "-v"], "Unit Tests"),
        (["uv", "run", "mypy", "predicate_logic/"], "Type Checking (mypy)"),
        (
            [
                "uv",
                "run",
                "flake8",
                "predicate_logic/",
                "tests/",
                "examples/",
                "--max-line-length=88",
            ],
            "Linting (flake8)",
        ),
        (
            [
                "uv",
                "run",
                "black",
                "--check",
                "predicate_logic/",
                "tests/",
                "examples/",
                "main.py",
                "run_tests.py",
            ],
            "Code Formatting (black)",
        ),
        (["uv", "run", "python", "main.py"], "Demo Execution"),
    ]

    passed = 0
    total = len(checks)

    for cmd, description in checks:
        if run_command(cmd, description):
            passed += 1

    print("\n" + "=" * 60)
    print(f"📊 SUMMARY: {passed}/{total} checks passed")

    if passed == total:
        print("🎉 All checks passed! The code is ready for production.")
        return 0
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
