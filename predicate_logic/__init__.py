"""
Predicate Logic Library

A Python library for working with predicate logic, logical operators,
quantifiers, and relations using functional programming approaches.
"""

from .knowledge_base import PredicateLogic
from .logical_operators import (
    logical_and,
    logical_iff,
    logical_implies,
    logical_not,
    logical_or,
    logical_xor,
)
from .patterns import (
    length_predicate,
    pattern_predicate,
    range_predicate,
    type_predicate,
)
from .predicates import (
    compose_predicates,
    equals,
    greater_than,
    is_even,
    is_positive,
    less_than,
)
from .quantifiers import (
    count_where,
    exists,
    exists_unique,
    find_all,
    find_first,
    forall,
)
from .relations import (
    bind_variable,
    cartesian_predicate,
    grandparent_of,
    is_equivalence_relation,
    is_reflexive,
    is_symmetric,
    is_transitive,
    loves,
    parent_of,
)

__version__ = "1.0.0"
__author__ = "Your Name"

__all__ = [
    # Basic predicates
    "is_even",
    "is_positive",
    "greater_than",
    "less_than",
    "equals",
    "compose_predicates",
    # Logical operators
    "logical_and",
    "logical_or",
    "logical_not",
    "logical_implies",
    "logical_iff",
    "logical_xor",
    # Quantifiers
    "forall",
    "exists",
    "exists_unique",
    "count_where",
    "find_all",
    "find_first",
    # Relations
    "loves",
    "parent_of",
    "grandparent_of",
    "is_reflexive",
    "is_symmetric",
    "is_transitive",
    "is_equivalence_relation",
    "cartesian_predicate",
    "bind_variable",
    # Knowledge base
    "PredicateLogic",
    # Pattern matching
    "pattern_predicate",
    "type_predicate",
    "range_predicate",
    "length_predicate",
]
