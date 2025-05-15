# Queues

A queue is a linear data structure that follows the First In, First Out (FIFO) principle. The first element added to the queue is the first one to be removed.

## Basic Operations

1. **Enqueue**: Add an element to the back of the queue
2. **Dequeue**: Remove the front element from the queue
3. **Front/Peek**: Get the front element without removing it
4. **isEmpty**: Check if the queue is empty
5. **Size**: Get the number of elements in the queue

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Enqueue   | O(1)           |
| Dequeue   | O(1)*          |
| Front     | O(1)           |
| isEmpty   | O(1)           |
| Size      | O(1)           |

\* O(n) for array-based implementation without tracking front index

## Types of Queues

1. **Simple Queue**: Standard FIFO queue
2. **Circular Queue**: Uses a circular array to optimize space
3. **Priority Queue**: Elements have priorities; higher priority elements are dequeued first
4. **Double-ended Queue (Deque)**: Elements can be added or removed from both ends

## Implementation Approaches

### 1. Using a List (Array)

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # O(n) operation
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
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

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, item):
        new_node = Node(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        data = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        return data
    
    def front_element(self):
        if self.is_empty():
            return None
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def get_size(self):
        return self.size
```

### 3. Using collections.deque

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()  # O(1) operation
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

## Applications of Queues

1. **Process Scheduling**:
   - CPU scheduling
   - Disk scheduling
   - Print job scheduling

2. **Data Transfer**:
   - IO Buffers
   - Pipes
   - File IO

3. **Breadth-First Search (BFS)**:
   - Graph traversal
   - Shortest path algorithms

4. **Handling of Requests**:
   - Web servers
   - Service centers
   - Call centers

5. **Real-time Systems**:
   - Event handling
   - Interrupt handling
   - Message passing

## Common Queue Problems

### 1. Implementing a Queue using Stacks

```python
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue
    
    def enqueue(self, item):
        self.stack1.append(item)
    
    def dequeue(self):
        if not self.stack2:
            # Transfer all elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            return None
        
        return self.stack2.pop()
```

### 2. Circular Queue Implementation

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0
    
    def enqueue(self, item):
        if self.is_full():
            return False
        
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = item
        self.size += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        data = self.queue[self.front]
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        self.size -= 1
        return data
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
```

### 3. Priority Queue Implementation

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def enqueue(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.elements)[1]
        return None
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def size(self):
        return len(self.elements)
```

## Queue vs. Stack

| Queue (FIFO)                | Stack (LIFO)                |
|----------------------------|----------------------------|
| First In, First Out        | Last In, First Out         |
| Insert at rear, delete from front | Insert and delete from same end |
| Used for sequential processing | Used for backtracking      |
| Example: Print queue       | Example: Browser back button |

## Advantages of Queues

1. Maintains data in FIFO order
2. Efficient for sequential processing
3. Useful for managing asynchronous requests
4. Provides predictable data access patterns

## Limitations of Queues

1. Limited access (only front and rear elements)
2. No random access to elements
3. Fixed size in array implementation (unless using dynamic arrays)
4. Potential for queue overflow in fixed-size implementations