#!/usr/bin/env python3
"""
Exercises for stack implementations.
"""

class Stack:
    """Simple stack implementation using a list."""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


# Exercise 1: Implement a function to reverse a string using a stack
def reverse_string(s):
    """
    Reverse a string using a stack.
    
    Args:
        s: String to reverse
        
    Returns:
        Reversed string
    """
    # Your solution here
    pass


# Exercise 2: Check if a string of parentheses is balanced
def is_balanced(expression):
    """
    Check if an expression has balanced parentheses.
    
    Args:
        expression: String containing parentheses, brackets, and braces
        
    Returns:
        True if balanced, False otherwise
    """
    # Your solution here
    pass


# Exercise 3: Convert infix expression to postfix
def infix_to_postfix(expression):
    """
    Convert an infix expression to postfix notation.
    
    Args:
        expression: String containing infix expression
        
    Returns:
        String containing postfix expression
    """
    # Your solution here
    pass


# Exercise 4: Evaluate a postfix expression
def evaluate_postfix(expression):
    """
    Evaluate a postfix expression.
    
    Args:
        expression: String containing postfix expression
        
    Returns:
        Result of the expression
    """
    # Your solution here
    pass


# Exercise 5: Implement a min stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack:
    """
    Stack that can retrieve minimum element in O(1) time.
    """
    def __init__(self):
        # Your solution here
        pass
    
    def push(self, val):
        # Your solution here
        pass
    
    def pop(self):
        # Your solution here
        pass
    
    def top(self):
        # Your solution here
        pass
    
    def get_min(self):
        # Your solution here
        pass


# Exercise 6: Implement a stack using queues
class StackUsingQueues:
    """
    Implement a stack using only queue operations.
    """
    def __init__(self):
        # Your solution here
        pass
    
    def push(self, x):
        # Your solution here
        pass
    
    def pop(self):
        # Your solution here
        pass
    
    def top(self):
        # Your solution here
        pass
    
    def empty(self):
        # Your solution here
        pass


# Exercise 7: Sort a stack
def sort_stack(stack):
    """
    Sort a stack in ascending order (smallest on top).
    
    Args:
        stack: Stack to sort
        
    Returns:
        Sorted stack
    """
    # Your solution here
    pass


# Exercise 8: Next greater element
def next_greater_element(arr):
    """
    Find the next greater element for each element in the array.
    
    Args:
        arr: List of integers
        
    Returns:
        List where each element is the next greater element
        or -1 if no greater element exists
    """
    # Your solution here
    pass


# Solutions

def reverse_string_solution(s):
    """Solution for Exercise 1."""
    stack = Stack()
    
    # Push all characters onto stack
    for char in s:
        stack.push(char)
    
    # Pop characters to get reversed string
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


def is_balanced_solution(expression):
    """Solution for Exercise 2."""
    stack = Stack()
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != brackets[char]:
                return False
    
    return stack.is_empty()


def infix_to_postfix_solution(expression):
    """Solution for Exercise 3."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            if not stack.is_empty() and stack.peek() == '(':
                stack.pop()  # Remove '('
        else:  # Operator
            while (not stack.is_empty() and stack.peek() != '(' and 
                   precedence.get(char, 0) <= precedence.get(stack.peek(), 0)):
                postfix.append(stack.pop())
            stack.push(char)
    
    while not stack.is_empty():
        postfix.append(stack.pop())
    
    return ''.join(postfix)


def evaluate_postfix_solution(expression):
    """Solution for Exercise 4."""
    stack = Stack()
    
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            if stack.size() < 2:
                raise ValueError("Invalid postfix expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)
            elif char == '^':
                stack.push(a ** b)
    
    if stack.size() != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack.pop()


class MinStackSolution:
    """Solution for Exercise 5."""
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        
        # Update min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if not self.stack:
            return None
        
        val = self.stack.pop()
        
        # Update min_stack if we're removing the minimum
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        
        return val
    
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    
    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


from collections import deque

class StackUsingQueuesSolution:
    """Solution for Exercise 6."""
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        # Add new element to the queue
        self.queue.append(x)
        
        # Rotate the queue to make the new element at the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        if not self.queue:
            return None
        return self.queue.popleft()
    
    def top(self):
        if not self.queue:
            return None
        return self.queue[0]
    
    def empty(self):
        return len(self.queue) == 0


def sort_stack_solution(stack):
    """Solution for Exercise 7."""
    temp_stack = Stack()
    
    while not stack.is_empty():
        # Pop an element from the original stack
        temp = stack.pop()
        
        # Move elements from temp_stack back to stack if they are greater than temp
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        
        # Push temp onto temp_stack
        temp_stack.push(temp)
    
    # Move all elements from temp_stack back to stack
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    
    return stack


def next_greater_element_solution(arr):
    """Solution for Exercise 8."""
    n = len(arr)
    result = [-1] * n
    stack = []
    
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result


if __name__ == "__main__":
    # Test Exercise 1: Reverse a string
    print("Testing Exercise 1: Reverse a string")
    test_str = "Hello, World!"
    reversed_str = reverse_string_solution(test_str)
    print(f"Original: {test_str}")
    print(f"Reversed: {reversed_str}")
    
    # Test Exercise 2: Check balanced parentheses
    print("\nTesting Exercise 2: Check balanced parentheses")
    expressions = ["()", "()[]{}", "(]", "([)]", "{[]}", ""]
    
    for expr in expressions:
        print(f"'{expr}' is {'balanced' if is_balanced_solution(expr) else 'not balanced'}")
    
    # Test Exercise 3: Infix to postfix conversion
    print("\nTesting Exercise 3: Infix to postfix conversion")
    infix_expressions = ["A+B", "A+B*C", "(A+B)*C", "A+B*(C-D)"]
    
    for expr in infix_expressions:
        postfix = infix_to_postfix_solution(expr)
        print(f"Infix: {expr} -> Postfix: {postfix}")
    
    # Test Exercise 4: Evaluate postfix expression
    print("\nTesting Exercise 4: Evaluate postfix expression")
    postfix_expressions = ["23+", "23*5+", "23+5*"]
    
    for expr in postfix_expressions:
        result = evaluate_postfix_solution(expr)
        print(f"Postfix: {expr} = {result}")
    
    # Test Exercise 5: Min Stack
    print("\nTesting Exercise 5: Min Stack")
    min_stack = MinStackSolution()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"Min value: {min_stack.get_min()}")  # -3
    min_stack.pop()
    print(f"Top value: {min_stack.top()}")  # 0
    print(f"Min value: {min_stack.get_min()}")  # -2
    
    # Test other exercises as needed