# Python Assertions Cheatsheet

## Basic Syntax

```python
assert condition
assert condition, "Error message"
```

## Common Assertion Patterns

### Type Checking
```python
assert isinstance(x, int), "x must be an integer"
assert isinstance(x, (int, float)), "x must be a number"
assert isinstance(x, list), "x must be a list"
assert isinstance(x, dict), "x must be a dictionary"
assert callable(x), "x must be callable"
```

### Value Validation
```python
assert x > 0, "x must be positive"
assert 0 <= x <= 100, "x must be between 0 and 100"
assert len(x) > 0, "x cannot be empty"
assert x in valid_values, "x must be one of the valid values"
```

### Collection Validation
```python
assert all(x > 0 for x in numbers), "All numbers must be positive"
assert any(condition(x) for x in items), "At least one item must meet the condition"
assert len(items) == expected_count, "Wrong number of items"
```

### Dictionary Validation
```python
assert "key" in my_dict, "Dictionary must contain 'key'"
assert all(key in my_dict for key in required_keys), "Missing required keys"
assert set(my_dict.keys()) == set(expected_keys), "Keys don't match expected keys"
```

### String Validation
```python
assert text.startswith("prefix"), "Text must start with 'prefix'"
assert text.endswith("suffix"), "Text must end with 'suffix'"
assert "@" in email, "Invalid email format"
```

### File Operations
```python
assert os.path.exists(file_path), f"File {file_path} does not exist"
assert os.path.isfile(file_path), f"{file_path} is not a file"
assert os.path.isdir(directory), f"{directory} is not a directory"
```

### Function Preconditions
```python
def my_function(a, b):
    assert a != 0, "a cannot be zero"
    assert b is not None, "b cannot be None"
    # Function body...
```

### Function Postconditions
```python
def calculate_average(numbers):
    result = sum(numbers) / len(numbers)
    assert min(numbers) <= result <= max(numbers), "Average must be between min and max values"
    return result
```

### Class Invariants
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
        self._check_invariants()
    
    def deposit(self, amount):
        self._balance += amount
        self._check_invariants()
    
    def withdraw(self, amount):
        self._balance -= amount
        self._check_invariants()
    
    def _check_invariants(self):
        assert self._balance >= 0, "Balance cannot be negative"
```

## When NOT to Use Assertions

- ❌ For data validation in production code
- ❌ For handling expected runtime errors
- ❌ For code with side effects
- ❌ For checking user inputs

## Best Practices

- ✓ Include descriptive error messages
- ✓ Use assertions for programmer errors, not user errors
- ✓ Keep assertions simple and focused
- ✓ Remember assertions can be disabled with -O flag
- ✓ Use assertions to document assumptions

## Running Python with Assertions Disabled

```bash
python -O script.py
```

## Assertions vs. Exceptions

| Assertions | Exceptions |
|------------|------------|
| For programmer errors | For expected runtime errors |
| Can be disabled | Always active |
| Internal checks | User-facing errors |
| `assert condition` | `if condition: raise Error` |
| Development/debugging | Production code |