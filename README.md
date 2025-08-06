"""
Predicate Logic Library

A Python library for working with predicate logic, logical operators,
quantifiers, and binary relations using functional programming approaches.

Features:
- Basic predicates and higher-order predicate functions
- Logical operators (AND, OR, NOT, IMPLIES, IFF, XOR)
- Quantifiers (universal, existential, unique existence)
- Binary relations and relation properties
- Simple knowledge base system
- Pattern matching predicates (Python 3.10+)
- Full type annotations for better IDE support and static analysis

## Installation

### Using uv (recommended)
```bash
uv sync --dev
```

### Using pip
```bash
pip install -e .
```

### Development dependencies
```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from predicate_logic import (
    is_even, is_positive, logical_and, forall, exists
)

# Create compound predicates
is_even_and_positive = logical_and(is_even, is_positive)

# Use with data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_positive_numbers = [n for n in numbers if is_even_and_positive(n)]
print(even_positive_numbers)  # [2, 4, 6, 8, 10]

# Use quantifiers
print(forall(is_positive, numbers))  # True
print(exists(is_even, numbers))     # True
```

## Running Examples

```bash
# With uv
uv run python main.py

# With regular python
python main.py
```

## Running Tests

```bash
# With uv
uv run pytest tests/ -v

# With regular python
python -m unittest discover tests/

# With coverage
uv run pytest tests/ --cov=predicate_logic --cov-report=term-missing
```

## Quality Checks

Run all quality checks at once:

```bash
# With uv
uv run python check_all.py

# Individual checks
uv run pytest tests/ -v          # Tests
uv run mypy predicate_logic/      # Type checking
uv run flake8 predicate_logic/    # Linting
uv run black --check .            # Code formatting
```

## Development

### Type Checking
This library is fully typed using Python type hints. All functions have proper type annotations:

```python
from typing import Callable, TypeVar

T = TypeVar('T')
Predicate = Callable[[T], bool]

def logical_and(pred1: Predicate[T], pred2: Predicate[T]) -> Predicate[T]:
    """Conjunction: P ∧ Q"""
    return lambda x: pred1(x) and pred2(x)
```

### Code Style
- Code formatted with `black`
- Linted with `flake8`
- Type checked with `mypy`
- 88 character line limit

## Project Structure

```
predicate-logic/
├── predicate_logic/          # Main package
│   ├── __init__.py          # Package initialization
│   ├── predicates.py        # Basic predicates
│   ├── logical_operators.py # Logical operators
│   ├── quantifiers.py       # Quantifier functions
│   ├── relations.py         # Binary relations
│   ├── knowledge_base.py    # Knowledge base system
│   └── patterns.py          # Pattern matching predicates
├── examples/                # Example scripts
│   ├── basic_examples.py    # Basic usage examples
│   ├── family_relations.py  # Family tree examples
│   └── knowledge_base_example.py # KB examples
├── tests/                   # Unit tests
│   ├── test_predicates.py
│   ├── test_logical_operators.py
│   └── test_quantifiers.py
├── main.py                  # Main demo script
├── run_tests.py            # Test runner
├── check_all.py            # Quality check runner
└── README.md               # This file
```

## License

MIT License
