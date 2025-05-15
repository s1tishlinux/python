# Stacks

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. The last element added to the stack is the first one to be removed.

## Basic Operations

1. **Push**: Add an element to the top of the stack
2. **Pop**: Remove the top element from the stack
3. **Peek/Top**: Get the top element without removing it
4. **isEmpty**: Check if the stack is empty

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Push      | O(1)           |
| Pop       | O(1)           |
| Peek      | O(1)           |
| isEmpty   | O(1)           |
| Search    | O(n)           |

## Implementation Approaches

### 1. Using a List (Array)

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

### 2. Using a Linked List

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

## Applications of Stacks

1. **Function Call Management**: 
   - Call stack for tracking function calls and returns
   - Recursion implementation

2. **Expression Evaluation and Conversion**:
   - Infix to Postfix/Prefix conversion
   - Evaluating postfix expressions
   - Checking balanced parentheses

3. **Undo Mechanisms**:
   - Implementing undo functionality in applications
   - Browser history (back button)

4. **Backtracking Algorithms**:
   - Maze solving
   - Game tree exploration (e.g., chess)

5. **Memory Management**:
   - Managing memory allocation and deallocation

6. **Parsing**:
   - Syntax parsing in compilers
   - HTML/XML parsing

## Common Stack Problems

### 1. Balanced Parentheses

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

### 2. Infix to Postfix Conversion

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

### 3. Evaluate Postfix Expression

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

## Stack vs. Queue

| Stack (LIFO)                | Queue (FIFO)                |
|----------------------------|----------------------------|
| Last In, First Out         | First In, First Out        |
| Insert and delete from one end | Insert at one end, delete from other |
| Used for backtracking      | Used for sequential processing |
| Example: Browser back button | Example: Print queue       |

## Advantages of Stacks

1. Simple and easy to implement
2. Efficient for LIFO operations
3. Memory efficient (no gaps)
4. Useful for many algorithms and applications

## Limitations of Stacks

1. Limited access (only top element)
2. No random access to elements
3. Fixed size in array implementation (unless using dynamic arrays)
4. Potential for stack overflow in recursive algorithms