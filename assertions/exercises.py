"""
Python Assertions - Practice Exercises
=====================================

This file contains exercises to practice using assertions in Python.
Try to solve each exercise before looking at the solution.
"""

# ===============================
# Exercise 1: Basic Assertions
# ===============================
print("Exercise 1: Basic Assertions")
print("----------------------------")
print("Write assertions to verify:")
print("1. The variable 'name' is a string")
print("2. The variable 'age' is at least 18")
print("3. The variable 'email' contains an '@' symbol")
print()

# Your solution here:
name = "Alice"
age = 25
email = "alice@example.com"

# Write your assertions below:



# Solution:
"""
assert isinstance(name, str), "Name must be a string"
assert age >= 18, "Age must be at least 18"
assert '@' in email, "Email must contain @ symbol"
"""

# ===============================
# Exercise 2: Function Validation
# ===============================
print("Exercise 2: Function Validation")
print("------------------------------")
print("Complete the function to calculate the average of a list of numbers.")
print("Use assertions to verify that:")
print("1. The input is a list")
print("2. The list is not empty")
print("3. All elements in the list are numbers (int or float)")
print()

def calculate_average(numbers):
    # Write your assertions here:
    
    
    # Calculate the average
    return sum(numbers) / len(numbers)

# Test cases:
try:
    print(f"Average of [1, 2, 3, 4, 5]: {calculate_average([1, 2, 3, 4, 5])}")
    print(f"Average of [10]: {calculate_average([10])}")
    # Uncomment to test error cases:
    # print(calculate_average("not a list"))
    # print(calculate_average([]))
    # print(calculate_average([1, 2, "three", 4]))
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Solution:
"""
def calculate_average(numbers):
    assert isinstance(numbers, list), "Input must be a list"
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(x, (int, float)) for x in numbers), "All elements must be numbers"
    
    return sum(numbers) / len(numbers)
"""

print()

# ===============================
# Exercise 3: Class Invariants
# ===============================
print("Exercise 3: Class Invariants")
print("---------------------------")
print("Complete the BankAccount class to maintain these invariants:")
print("1. Balance should never be negative")
print("2. Withdrawal amount must be positive")
print("3. Deposit amount must be positive")
print()

class BankAccount:
    def __init__(self, initial_balance=0):
        # Add assertion here:
        
        self.balance = initial_balance
    
    def withdraw(self, amount):
        # Add assertions here:
        
        
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        # Add assertion here:
        
        
        self.balance += amount
        return self.balance

# Test cases:
try:
    account = BankAccount(100)
    print(f"Initial balance: {account.balance}")
    print(f"After withdrawal of 30: {account.withdraw(30)}")
    print(f"After deposit of 50: {account.deposit(50)}")
    
    # Uncomment to test error cases:
    # account = BankAccount(-50)  # Negative initial balance
    # account.withdraw(-20)  # Negative withdrawal
    # account.withdraw(200)  # Overdraft
    # account.deposit(-30)  # Negative deposit
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Solution:
"""
class BankAccount:
    def __init__(self, initial_balance=0):
        assert initial_balance >= 0, "Initial balance cannot be negative"
        self.balance = initial_balance
    
    def withdraw(self, amount):
        assert amount > 0, "Withdrawal amount must be positive"
        assert self.balance >= amount, "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        assert amount > 0, "Deposit amount must be positive"
        self.balance += amount
        return self.balance
"""

print()

# ===============================
# Exercise 4: Data Processing
# ===============================
print("Exercise 4: Data Processing")
print("--------------------------")
print("Complete the function to process a list of student records.")
print("Each record is a dictionary with 'name', 'grades', and 'active' keys.")
print("Use assertions to verify that:")
print("1. Each record is a dictionary")
print("2. Each record has the required keys")
print("3. Grades is a list of numbers between 0 and 100")
print()

def calculate_student_averages(students):
    """
    Calculate the average grade for each active student.
    Returns a dictionary mapping student names to their average grade.
    """
    # Write your assertions and code here:
    
    
    
    
    # Calculate averages for active students
    results = {}
    for student in students:
        if student['active']:
            results[student['name']] = sum(student['grades']) / len(student['grades'])
    return results

# Test case:
students = [
    {'name': 'Alice', 'grades': [85, 90, 95], 'active': True},
    {'name': 'Bob', 'grades': [70, 75, 80], 'active': True},
    {'name': 'Charlie', 'grades': [90, 92, 88], 'active': False}  # Inactive student
]

try:
    averages = calculate_student_averages(students)
    print("Student averages:")
    for name, avg in averages.items():
        print(f"{name}: {avg:.1f}")
    
    # Uncomment to test error cases:
    # Invalid record type
    # calculate_student_averages([{'name': 'Alice', 'grades': [85, 90, 95], 'active': True}, "not a dict"])
    
    # Missing key
    # calculate_student_averages([{'name': 'Alice', 'active': True}])
    
    # Invalid grades
    # calculate_student_averages([{'name': 'Alice', 'grades': [85, 105, 95], 'active': True}])
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Solution:
"""
def calculate_student_averages(students):
    assert isinstance(students, list), "Input must be a list"
    
    for student in students:
        assert isinstance(student, dict), "Each student record must be a dictionary"
        assert all(key in student for key in ['name', 'grades', 'active']), "Missing required keys"
        assert isinstance(student['grades'], list), "Grades must be a list"
        assert all(isinstance(grade, (int, float)) for grade in student['grades']), "Grades must be numbers"
        assert all(0 <= grade <= 100 for grade in student['grades']), "Grades must be between 0 and 100"
    
    results = {}
    for student in students:
        if student['active']:
            results[student['name']] = sum(student['grades']) / len(student['grades'])
    return results
"""

print()
print("End of exercises")