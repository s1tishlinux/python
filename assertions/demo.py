"""
Python Assertions Tutorial
=========================

This script demonstrates how to use assertions in Python for:
1. Basic validation
2. Debugging
3. Testing
4. Documentation
"""

# ===============================
# 1. BASIC ASSERTION SYNTAX
# ===============================
print("1. BASIC ASSERTION SYNTAX")
print("--------------------------")

# Basic assertion - will pass silently
x = 10
assert x == 10
print("✓ assert x == 10 passed")

# Assertion with message - will pass silently
y = 5
assert y > 0, "y must be positive"
print("✓ assert y > 0 passed")

# Uncomment to see assertion error
# assert x == 20, "x should be 20"

print("\n")

# ===============================
# 2. USING ASSERTIONS FOR VALIDATION
# ===============================
print("2. USING ASSERTIONS FOR VALIDATION")
print("---------------------------------")

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    # Validate inputs with assertions
    assert length > 0, "Length must be positive"
    assert width > 0, "Width must be positive"
    
    return length * width

# Valid inputs
area = calculate_rectangle_area(5, 3)
print(f"Rectangle area: {area}")

# Uncomment to see assertion error
# area = calculate_rectangle_area(-5, 3)

print("\n")

# ===============================
# 3. ASSERTIONS FOR DEBUGGING
# ===============================
print("3. ASSERTIONS FOR DEBUGGING")
print("--------------------------")

def process_data(data_list):
    """Process a list of numbers."""
    # Debugging assertion to check input type
    assert isinstance(data_list, list), "Input must be a list"
    
    # Debugging assertion to check list contents
    assert all(isinstance(item, (int, float)) for item in data_list), "All items must be numbers"
    
    # Process the data
    return sum(data_list) / len(data_list) if data_list else 0

# Valid input
result = process_data([1, 2, 3, 4, 5])
print(f"Average: {result}")

# Uncomment to see assertion errors
# result = process_data("not a list")
# result = process_data([1, 2, "three", 4])

print("\n")

# ===============================
# 4. ASSERTIONS VS EXCEPTIONS
# ===============================
print("4. ASSERTIONS VS EXCEPTIONS")
print("--------------------------")

def divide(a, b):
    """
    Divide a by b.
    
    For production code, use exceptions for expected errors:
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    # Assertions are for programmer errors or impossible conditions
    assert isinstance(a, (int, float)), "a must be a number"
    assert isinstance(b, (int, float)), "b must be a number"
    
    return a / b

# Valid division
print(f"10 / 2 = {divide(10, 2)}")

# Expected error handling
try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Caught expected error: {e}")

# Uncomment to see assertion error (programmer error)
# result = divide("10", 2)

print("\n")

# ===============================
# 5. ASSERTIONS IN TESTING
# ===============================
print("5. ASSERTIONS IN TESTING")
print("-----------------------")

def test_rectangle_area():
    """Test function for rectangle area calculation."""
    # Test case 1: Regular rectangle
    assert calculate_rectangle_area(4, 5) == 20, "4×5 should be 20"
    
    # Test case 2: Square
    assert calculate_rectangle_area(3, 3) == 9, "3×3 should be 9"
    
    # Test case 3: Decimal values
    assert calculate_rectangle_area(2.5, 3) == 7.5, "2.5×3 should be 7.5"
    
    print("All rectangle area tests passed!")

# Run the test
test_rectangle_area()

print("\n")

# ===============================
# 6. ADVANCED ASSERTIONS
# ===============================
print("6. ADVANCED ASSERTIONS")
print("---------------------")

# Complex condition
def is_valid_user(user):
    """Check if user dictionary has all required fields."""
    assert isinstance(user, dict), "User must be a dictionary"
    assert "name" in user, "User must have a name"
    assert "age" in user, "User must have an age"
    assert user["age"] >= 18, "User must be an adult"
    
    return True

# Valid user
valid_user = {"name": "Alice", "age": 30, "email": "alice@example.com"}
print(f"Is valid user: {is_valid_user(valid_user)}")

# Uncomment to see assertion errors
# invalid_user1 = {"name": "Bob"}  # Missing age
# is_valid_user(invalid_user1)

# invalid_user2 = {"name": "Charlie", "age": 16}  # Underage
# is_valid_user(invalid_user2)

print("\n")

# ===============================
# 7. DISABLING ASSERTIONS
# ===============================
print("7. DISABLING ASSERTIONS")
print("----------------------")
print("Run Python with -O flag to disable assertions:")
print("python -O python_assertions_demo.py")
print("\nWhen assertions are disabled:")
print("- assert statements are not executed")
print("- This is useful for production environments")
print("- Don't use assertions for critical validation")

print("\n")

# ===============================
# 8. BEST PRACTICES
# ===============================
print("8. BEST PRACTICES")
print("----------------")
print("✓ Use assertions for programmer errors, not user errors")
print("✓ Include helpful error messages")
print("✓ Don't use assertions for data validation in production code")
print("✓ Use assertions to document assumptions")
print("✓ Remember assertions can be disabled")

print("\n")
print("End of Python Assertions Tutorial")