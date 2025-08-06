# Basic predicate representation
def is_even(x):
    """Predicate: x is even"""
    return x % 2 == 0

def is_positive(x):
    """Predicate: x is positive"""
    return x > 0

def greater_than(threshold):
    """Higher-order predicate: returns a predicate function"""
    return lambda x: x > threshold

# Logical operators as higher-order functions
def logical_and(pred1, pred2):
    """Conjunction: P ∧ Q"""
    return lambda x: pred1(x) and pred2(x)

def logical_or(pred1, pred2):
    """Disjunction: P ∨ Q"""
    return lambda x: pred1(x) or pred2(x)

def logical_not(pred):
    """Negation: ¬P"""
    return lambda x: not pred(x)

def logical_implies(pred1, pred2):
    """Implication: P → Q (equivalent to ¬P ∨ Q)"""
    return lambda x: (not pred1(x)) or pred2(x)

# Quantifiers using functional programming
def forall(predicate, domain):
    """Universal quantifier: ∀x ∈ domain, P(x)"""
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    """Existential quantifier: ∃x ∈ domain, P(x)"""
    return any(predicate(x) for x in domain)

def exists_unique(predicate, domain):
    """Unique existence: ∃!x ∈ domain, P(x)"""
    return sum(1 for x in domain if predicate(x)) == 1

# Example usage
if __name__ == "__main__":
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

# Advanced: Predicate composition using decorators
def compose_predicates(*predicates):
    """Compose multiple predicates with AND logic"""
    def composed_predicate(x):
        return all(pred(x) for pred in predicates)
    return composed_predicate

# Multi-argument predicates
def loves(person1, person2):
    """Binary predicate: person1 loves person2"""
    # This would typically check some data structure
    relationships = {("Alice", "Bob"), ("Bob", "Charlie"), ("Alice", "Alice")}
    return (person1, person2) in relationships

def is_reflexive(relation, domain):
    """Check if a binary relation is reflexive"""
    return forall(lambda x: relation(x, x), domain)

def is_symmetric(relation, domain):
    """Check if a binary relation is symmetric"""
    return forall(
        lambda x: forall(
            lambda y: logical_implies(
                lambda _: relation(x, y),
                lambda _: relation(y, x)
            )(None),
            domain
        ),
        domain
    )

# Functional approach to first-order logic
class PredicateLogic:
    """Class-based approach for more complex predicate logic"""
    
    def __init__(self):
        self.facts = set()
        self.rules = []
    
    def add_fact(self, fact):
        """Add a ground fact"""
        self.facts.add(fact)
    
    def add_rule(self, condition, conclusion):
        """Add a rule: if condition then conclusion"""
        self.rules.append((condition, conclusion))
    
    def query(self, predicate, *args):
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

# Example with the class-based approach
kb = PredicateLogic()

# Add facts
kb.add_fact(("human", ("socrates",)))
kb.add_fact(("human", ("plato",)))

# Add rule: if human(x) then mortal(x)
kb.add_rule(
    lambda x: kb.query("human", x),
    ("mortal", ("socrates",))  # This would need to be generalized
)

# Functional programming with itertools for complex logic
from itertools import product, combinations
from functools import reduce

def cartesian_predicate(pred1, pred2):
    """Create predicate over cartesian product of domains"""
    def cart_pred(xy_pair):
        x, y = xy_pair
        return pred1(x) and pred2(y)
    return cart_pred

def bind_variable(predicate, var_index, value):
    """Bind a specific variable in a multi-argument predicate"""
    def bound_predicate(*args):
        new_args = list(args)
        new_args.insert(var_index, value)
        return predicate(*new_args)
    return bound_predicate

# Example: Working with relations
def parent_of(parent, child):
    """Example binary relation"""
    family_tree = {
        ("John", "Alice"),
        ("John", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "David")
    }
    return (parent, child) in family_tree

def grandparent_of(grandparent, grandchild):
    """Derived relation: grandparent if parent of parent"""
    people = ["John", "Alice", "Bob", "Charlie", "David"]
    return exists(
        lambda middle: parent_of(grandparent, middle) and parent_of(middle, grandchild),
        people
    )

# Test the family relations
people = ["John", "Alice", "Bob", "Charlie", "David"]
print(f"\nJohn is grandparent of Charlie: {grandparent_of('John', 'Charlie')}")
print(f"Alice is grandparent of David: {grandparent_of('Alice', 'David')}")

# Pattern matching approach (Python 3.10+)
def pattern_predicate(pattern):
    """Create predicate based on pattern matching"""
    def pred(value):
        match pattern:
            case int() if pattern > 0:
                return isinstance(value, int) and value > 0
            case str() if len(pattern) > 0:
                return isinstance(value, str) and len(value) > 0
            case _:
                return value == pattern
    return pred