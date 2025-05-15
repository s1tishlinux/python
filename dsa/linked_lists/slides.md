# Linked Lists
## A Fundamental Data Structure

---

## What is a Linked List?

- Linear data structure
- Elements stored in nodes
- Each node contains data and reference(s) to other node(s)
- Not stored in contiguous memory locations
- Dynamic size

---

## Types of Linked Lists

1. **Singly Linked List**
   - Each node points to the next node
   - Last node points to null

2. **Doubly Linked List**
   - Each node points to both next and previous nodes
   - First node's previous points to null
   - Last node's next points to null

3. **Circular Linked List**
   - Last node points back to the first node
   - Can be singly or doubly linked

---

## Singly Linked List: Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
```

Visual representation:
```
head → [data|next] → [data|next] → [data|next] → None
```

---

## Doubly Linked List: Structure

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

Visual representation:
```
None ← [prev|data|next] ⇄ [prev|data|next] ⇄ [prev|data|next] → None
       ↑                                                  
      head                                               
```

---

## Basic Operations: Insertion

### Insert at Beginning (Singly Linked List)
```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

Time Complexity: O(1)

---

## Basic Operations: Insertion

### Insert at End (Singly Linked List)
```python
def insert_at_end(self, data):
    new_node = Node(data)
    
    if not self.head:
        self.head = new_node
        return
    
    current = self.head
    while current.next:
        current = current.next
    
    current.next = new_node
```

Time Complexity: O(n)

---

## Basic Operations: Deletion

### Delete at Beginning (Singly Linked List)
```python
def delete_at_beginning(self):
    if not self.head:
        return None
    
    data = self.head.data
    self.head = self.head.next
    return data
```

Time Complexity: O(1)

---

## Basic Operations: Deletion

### Delete at End (Singly Linked List)
```python
def delete_at_end(self):
    if not self.head:
        return None
    
    if not self.head.next:
        data = self.head.data
        self.head = None
        return data
    
    current = self.head
    while current.next.next:
        current = current.next
    
    data = current.next.data
    current.next = None
    return data
```

Time Complexity: O(n)

---

## Basic Operations: Search

```python
def search(self, data):
    current = self.head
    position = 0
    
    while current:
        if current.data == data:
            return position
        current = current.next
        position += 1
    
    return -1  # Not found
```

Time Complexity: O(n)

---

## Time Complexity Comparison

| Operation | Singly Linked List | Doubly Linked List | Array |
|-----------|-------------------|-------------------|-------|
| Access | O(n) | O(n) | O(1) |
| Insert at beginning | O(1) | O(1) | O(n) |
| Insert at end | O(n)* | O(1)** | O(1)*** |
| Insert in middle | O(n) | O(n) | O(n) |
| Delete at beginning | O(1) | O(1) | O(n) |
| Delete at end | O(n)* | O(1)** | O(1) |
| Delete in middle | O(n) | O(n) | O(n) |
| Search | O(n) | O(n) | O(n) |

\* O(1) with tail pointer  
\** With tail pointer  
\*** Amortized for dynamic arrays

---

## Common Linked List Algorithms

1. **Reversing a Linked List**
2. **Detecting Cycles**
3. **Finding the Middle Node**
4. **Merging Sorted Lists**
5. **Removing Duplicates**

---

## Algorithm: Reversing a Linked List

```python
def reverse(self):
    prev = None
    current = self.head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    self.head = prev
```

Time Complexity: O(n)  
Space Complexity: O(1)

---

## Algorithm: Detecting Cycles (Floyd's Algorithm)

```python
def has_cycle(self):
    if not self.head or not self.head.next:
        return False
    
    slow = self.head
    fast = self.head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

Time Complexity: O(n)  
Space Complexity: O(1)

---

## Algorithm: Finding the Middle Node

```python
def find_middle(self):
    if not self.head:
        return None
    
    slow = self.head
    fast = self.head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

Time Complexity: O(n)  
Space Complexity: O(1)

---

## Advantages of Linked Lists

- Dynamic size
- Efficient insertions/deletions
- No pre-allocation of memory
- Flexible memory management
- Easy implementation of stacks, queues

---

## Disadvantages of Linked Lists

- Random access is not allowed
- Extra memory for pointers
- Not cache-friendly
- Reverse traversal is difficult (singly linked)
- More complex implementation than arrays

---

## Applications of Linked Lists

- Implementation of stacks and queues
- Dynamic memory allocation
- Undo functionality in applications
- Hash tables (chaining)
- Adjacency lists for graphs
- Music playlists
- Browser history

---

## When to Use Linked Lists

- When insertions/deletions are frequent
- When data size is unknown
- When random access is not required
- When memory efficiency is important
- When implementing certain data structures

---

## When to Use Arrays Instead

- When random access is required
- When memory locality is important
- When the size is fixed
- When simple implementation is preferred
- When cache performance matters

---

## Thank You!

### Questions?