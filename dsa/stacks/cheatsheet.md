# Stack Cheatsheet

## Definition
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.

## Basic Operations

| Operation | Description | Time Complexity |
|-----------|-------------|----------------|
| push(item) | Add item to top | O(1) |
| pop() | Remove and return top item | O(1) |
| peek()/top() | Return top item without removing | O(1) |
| isEmpty() | Check if stack is empty | O(1) |
| size() | Return number of elements | O(1) |

## Implementation in Python

### Using List
```python
class Stack:
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
```

### Using Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def get_size(self):
        return self.size
```

### Using collections.deque
```python
from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
    
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
```

## Common Stack Algorithms

### Check Balanced Parentheses
```python
def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0
```

### Infix to Postfix Conversion
```python
def infix_to_postfix(expression):
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
            stack.pop()  # Remove '('
        else:  # Operator
            while stack and stack[-1] != '(' and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)
```

### Evaluate Postfix Expression
```python
def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
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
    
    return stack.pop()
```

### Reverse a String
```python
def reverse_string(s):
    stack = []
    
    # Push all characters onto stack
    for char in s:
        stack.append(char)
    
    # Pop characters to get reversed string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str
```

### Next Greater Element
```python
def next_greater_element(arr):
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
```

### Stock Span Problem
```python
def calculate_span(prices):
    n = len(prices)
    spans = [1] * n
    stack = []
    
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        spans[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    
    return spans
```

## Stack vs. Recursion

Many recursive algorithms can be rewritten using stacks:

```python
# Recursive factorial
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

# Stack-based factorial
def factorial_stack(n):
    stack = []
    result = 1
    
    while n > 0:
        stack.append(n)
        n -= 1
    
    while stack:
        result *= stack.pop()
    
    return result
```

## Memory Management in Stack

- Stack memory is allocated/deallocated in LIFO order
- Function calls use a call stack
- Local variables are stored on the stack
- Stack overflow occurs when too many function calls exceed stack size

## Common Stack Applications

1. Function call management (call stack)
2. Expression evaluation
3. Syntax parsing
4. Backtracking algorithms
5. Undo mechanisms
6. Browser history
7. Memory management