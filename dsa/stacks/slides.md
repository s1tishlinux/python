# Stacks
## A Fundamental Data Structure

---

## What is a Stack?

- Linear data structure
- Follows Last In, First Out (LIFO) principle
- Like a stack of plates
- Operations occur at one end (top)
- Restricted access data structure

---

## Stack Operations

- **push(item)**: Add item to top
- **pop()**: Remove and return top item
- **peek()/top()**: Return top item without removing
- **isEmpty()**: Check if stack is empty
- **size()**: Return number of elements

---

## Stack Implementation: Using Array

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

---

## Stack Implementation: Using Linked List

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
```

---

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Push      | O(1)           |
| Pop       | O(1)           |
| Peek      | O(1)           |
| isEmpty   | O(1)           |
| Search    | O(n)           |

---

## Stack vs. Queue

| Stack (LIFO)                | Queue (FIFO)                |
|----------------------------|----------------------------|
| Last In, First Out         | First In, First Out        |
| Insert and delete from one end | Insert at one end, delete from other |
| Used for backtracking      | Used for sequential processing |
| Example: Browser back button | Example: Print queue       |

---

## Application: Function Calls

- Function calls are managed using a call stack
- Each function call creates a stack frame
- Local variables stored in the frame
- Return address stored in the frame
- Parameters stored in the frame

```
|                |
| function3()    | <- Top
|----------------|
| function2()    |
|----------------|
| function1()    |
|----------------|
| main()         |
|________________|
```

---

## Application: Expression Evaluation

- Infix: a + b * c
- Postfix: a b c * +
- Prefix: + a * b c

Converting infix to postfix:
1. Scan from left to right
2. If operand, add to output
3. If operator, pop operators with higher precedence
4. If '(', push to stack
5. If ')', pop until matching '('

---

## Application: Balanced Parentheses

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

---

## Application: Undo Functionality

- Each action is pushed onto a stack
- Undo pops the most recent action
- Redo can be implemented with a second stack

```
|                |
| Delete text    | <- Most recent (Undo this)
|----------------|
| Format text    |
|----------------|
| Insert image   |
|----------------|
| Type paragraph |
|________________|
```

---

## Application: Browser History

- Back button: Pop from history stack, push to forward stack
- Forward button: Pop from forward stack, push to history stack
- New page: Push to history stack, clear forward stack

```
History Stack         Forward Stack
|            |       |            |
| Page 3     |       |            |
|------------|       |------------|
| Page 2     |       |            |
|------------|       |------------|
| Page 1     |       |            |
|____________|       |____________|
```

---

## Stack-based Algorithms: Depth-First Search

```python
def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            
            # Add neighbors to stack
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
```

---

## Stack-based Algorithms: Infix to Postfix

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

---

## Stack-based Algorithms: Evaluate Postfix

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

---

## Advanced Stack: Min Stack

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
```

---

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

---

## Memory Management in Stack

- Stack memory is allocated/deallocated in LIFO order
- Function calls use a call stack
- Local variables are stored on the stack
- Stack overflow occurs when too many function calls exceed stack size

---

## Common Stack Applications

1. Function call management (call stack)
2. Expression evaluation
3. Syntax parsing
4. Backtracking algorithms
5. Undo mechanisms
6. Browser history
7. Memory management

---

## Thank You!

### Questions?