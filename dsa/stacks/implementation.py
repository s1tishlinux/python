#!/usr/bin/env python3
"""
Implementation of stack data structure using different approaches.
"""

class ArrayStack:
    """Stack implementation using a Python list."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
    
    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.items)


class Node:
    """A node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    """Stack implementation using a linked list."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.top = None
        self._size = 0
    
    def push(self, item):
        """Add an item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise Exception("Stack is empty")
        
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data
    
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.data
    
    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None
    
    def size(self):
        """Return the number of items in the stack."""
        return self._size
    
    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "[]"
        
        result = []
        current = self.top
        
        while current:
            result.append(str(current.data))
            current = current.next
        
        return "[" + ", ".join(result) + "] <- Top"


from collections import deque

class DequeStack:
    """Stack implementation using collections.deque."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = deque()
    
    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
    
    def __str__(self):
        """Return a string representation of the stack."""
        return str(list(self.items))


def is_balanced(expression):
    """
    Check if an expression has balanced parentheses.
    
    Args:
        expression: String containing parentheses, brackets, and braces
        
    Returns:
        True if balanced, False otherwise
    """
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0


def infix_to_postfix(expression):
    """
    Convert an infix expression to postfix notation.
    
    Args:
        expression: String containing infix expression
        
    Returns:
        String containing postfix expression
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # Remove '('
        else:  # Operator
            while stack and stack[-1] != '(' and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)


def evaluate_postfix(expression):
    """
    Evaluate a postfix expression.
    
    Args:
        expression: String containing postfix expression
        
    Returns:
        Result of the expression
    """
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
            elif char == '^':
                stack.append(a ** b)
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack.pop()


def next_greater_element(arr):
    """
    Find the next greater element for each element in the array.
    
    Args:
        arr: List of integers
        
    Returns:
        List where each element is the next greater element
        or -1 if no greater element exists
    """
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
    # Test ArrayStack
    print("Testing ArrayStack...")
    array_stack = ArrayStack()
    
    array_stack.push(1)
    array_stack.push(2)
    array_stack.push(3)
    
    print(f"Stack: {array_stack}")
    print(f"Size: {array_stack.size()}")
    print(f"Top element: {array_stack.peek()}")
    print(f"Popped element: {array_stack.pop()}")
    print(f"Stack after pop: {array_stack}")
    
    # Test LinkedListStack
    print("\nTesting LinkedListStack...")
    linked_stack = LinkedListStack()
    
    linked_stack.push(1)
    linked_stack.push(2)
    linked_stack.push(3)
    
    print(f"Stack: {linked_stack}")
    print(f"Size: {linked_stack.size()}")
    print(f"Top element: {linked_stack.peek()}")
    print(f"Popped element: {linked_stack.pop()}")
    print(f"Stack after pop: {linked_stack}")
    
    # Test DequeStack
    print("\nTesting DequeStack...")
    deque_stack = DequeStack()
    
    deque_stack.push(1)
    deque_stack.push(2)
    deque_stack.push(3)
    
    print(f"Stack: {deque_stack}")
    print(f"Size: {deque_stack.size()}")
    print(f"Top element: {deque_stack.peek()}")
    print(f"Popped element: {deque_stack.pop()}")
    print(f"Stack after pop: {deque_stack}")
    
    # Test balanced parentheses
    print("\nTesting balanced parentheses...")
    expressions = ["()", "()[]{}", "(]", "([)]", "{[]}", ""]
    
    for expr in expressions:
        print(f"'{expr}' is {'balanced' if is_balanced(expr) else 'not balanced'}")
    
    # Test infix to postfix conversion
    print("\nTesting infix to postfix conversion...")
    infix_expressions = ["A+B", "A+B*C", "(A+B)*C", "A+B*(C-D)", "A*B+C*D", "A*(B+C*D)"]
    
    for expr in infix_expressions:
        postfix = infix_to_postfix(expr)
        print(f"Infix: {expr} -> Postfix: {postfix}")
    
    # Test postfix evaluation
    print("\nTesting postfix evaluation...")
    postfix_expressions = ["23+", "23*5+", "23+5*", "234*+"]
    
    for expr in postfix_expressions:
        result = evaluate_postfix(expr)
        print(f"Postfix: {expr} = {result}")
    
    # Test next greater element
    print("\nTesting next greater element...")
    arrays = [[4, 5, 2, 25], [13, 7, 6, 12], [6, 8, 0, 1, 3]]
    
    for arr in arrays:
        result = next_greater_element(arr)
        print(f"Array: {arr}")
        print(f"Next greater elements: {result}")