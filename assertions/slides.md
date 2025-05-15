# Python Assertions
## A Powerful Debugging and Testing Tool

---

## What are Assertions?

- Debugging statements that test a condition
- If condition is True: program continues silently
- If condition is False: raises AssertionError
- Can include optional error message

```python
assert condition, "Optional error message"
```

---

## Basic Syntax

```python
# Simple assertion
assert x > 0

# Assertion with error message
assert y == 10, "y must equal 10"
```

---

## When Assertions Fail

```python
x = 5
assert x == 10, "x should be 10"
```

Output:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: x should be 10
```

---

## Use Case 1: Validating Function Inputs

```python
def calculate_rectangle_area(length, width):
    assert length > 0, "Length must be positive"
    assert width > 0, "Width must be positive"
    
    return length * width
```

---

## Use Case 2: Debugging

```python
def process_data(data_list):
    # Verify our assumptions
    assert isinstance(data_list, list), "Input must be a list"
    assert all(isinstance(item, (int, float)) for item in data_list), \
           "All items must be numbers"
    
    # Process the data
    return sum(data_list) / len(data_list)
```

---

## Use Case 3: Testing

```python
def test_rectangle_area():
    assert calculate_rectangle_area(4, 5) == 20, "4×5 should be 20"
    assert calculate_rectangle_area(3, 3) == 9, "3×3 should be 9"
    assert calculate_rectangle_area(2.5, 3) == 7.5, "2.5×3 should be 7.5"
    print("All tests passed!")
```

---

## Use Case 4: Documentation

```python
def update_user(user_dict):
    # Document our assumptions about the input
    assert "id" in user_dict, "User must have an ID"
    assert isinstance(user_dict["name"], str), "Name must be a string"
    
    # Update user in database
    # ...
```

---

## Assertions vs. Exceptions

### Assertions
- For programmer errors (bugs)
- Can be disabled in production
- Internal sanity checks

### Exceptions
- For expected runtime errors
- Always active in production
- User-facing error handling

---

## Assertions: The Wrong Way

```python
# DON'T DO THIS
def divide(a, b):
    assert b != 0, "Cannot divide by zero"  # Wrong!
    return a / b
```

## Exceptions: The Right Way

```python
# DO THIS INSTEAD
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

---

## Disabling Assertions

- Run Python with the `-O` flag:
  ```
  python -O script.py
  ```

- When disabled, assertions are not executed
- Don't use assertions for code that must run!

---

## Best Practices

- ✓ Use assertions for programmer errors, not user errors
- ✓ Include helpful error messages
- ✓ Don't use assertions for data validation in production
- ✓ Use assertions to document assumptions
- ✓ Don't use assertions with side effects
- ✓ Remember assertions can be disabled

---

## Thank You!

### Questions?