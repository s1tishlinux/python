# Queue Cheatsheet

## Definition
A queue is a linear data structure that follows the First In, First Out (FIFO) principle.

## Basic Operations

| Operation | Description | Time Complexity |
|-----------|-------------|----------------|
| enqueue(item) | Add item to back | O(1) |
| dequeue() | Remove and return front item | O(1)* |
| front()/peek() | Return front item without removing | O(1) |
| isEmpty() | Check if queue is empty | O(1) |
| size() | Return number of elements | O(1) |

\* O(n) for array-based implementation without tracking front index

## Implementation in Python

### Using List (Inefficient for large queues)
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

### Using Linked List
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

### Using collections.deque (Most Efficient)
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

## Types of Queues

### Circular Queue
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

### Priority Queue
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

### Double-ended Queue (Deque)
```python
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()
    
    def add_front(self, item):
        self.items.appendleft(item)
    
    def add_rear(self, item):
        self.items.append(item)
    
    def remove_front(self):
        if not self.is_empty():
            return self.items.popleft()
        return None
    
    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

## Common Queue Algorithms

### Breadth-First Search (BFS)
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Level Order Traversal of Binary Tree
```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### Implementing a Queue using Stacks
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
    
    def front(self):
        if not self.stack2:
            # Transfer all elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            return None
        
        return self.stack2[-1]
    
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
```

### Sliding Window Maximum
```python
from collections import deque

def max_sliding_window(nums, k):
    result = []
    window = deque()
    
    for i, num in enumerate(nums):
        # Remove elements outside the window
        while window and window[0] < i - k + 1:
            window.popleft()
        
        # Remove smaller elements
        while window and nums[window[-1]] < num:
            window.pop()
        
        window.append(i)
        
        # Add maximum of current window to result
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result
```

## Common Queue Applications

1. **Process Scheduling**: CPU scheduling, disk scheduling
2. **IO Buffers**: Managing data transfer
3. **Breadth-First Search**: Graph traversal algorithms
4. **Web Servers**: Request handling
5. **Print Spooling**: Managing print jobs
6. **Message Queues**: Asynchronous communication between systems
7. **Call Center Systems**: Managing customer service calls