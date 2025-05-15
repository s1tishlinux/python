# Linked Lists Cheatsheet

## Basic Structures

### Singly Linked List Node
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Doubly Linked List Node
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

## Singly Linked List Implementation

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_at_beginning(self):
        if self.is_empty():
            raise Exception("List is empty")
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def delete_at_end(self):
        if self.is_empty():
            raise Exception("List is empty")
        
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        data = current.next.data
        current.next = None
        self.size -= 1
        return data
    
    def delete_at_position(self, position):
        if self.is_empty():
            raise Exception("List is empty")
        
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            return self.delete_at_beginning()
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return data
    
    def search(self, data):
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1  # Not found
    
    def display(self):
        elements = []
        current = self.head
        
        while current:
            elements.append(current.data)
            current = current.next
        
        return elements
```

## Doubly Linked List Implementation

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def delete_at_beginning(self):
        if self.is_empty():
            raise Exception("List is empty")
        
        data = self.head.data
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return data
    
    def delete_at_end(self):
        if self.is_empty():
            raise Exception("List is empty")
        
        data = self.tail.data
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return data
```

## Common Algorithms

### Reverse a Linked List
```python
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev  # New head
```

### Detect Cycle (Floyd's Algorithm)
```python
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

### Find Middle Node
```python
def find_middle(head):
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

### Merge Two Sorted Lists
```python
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    # Attach remaining nodes
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    
    return dummy.next
```

### Remove Nth Node From End
```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    
    first = dummy
    second = dummy
    
    # Advance first pointer by n+1 steps
    for _ in range(n + 1):
        if not first:
            return head
        first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node
    second.next = second.next.next
    
    return dummy.next
```

## Time Complexity Summary

| Operation | Singly Linked List | Doubly Linked List |
|-----------|-------------------|-------------------|
| Access | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at beginning | O(1) | O(1) |
| Insert at end | O(n)* | O(1) |
| Insert in middle | O(n) | O(n) |
| Delete at beginning | O(1) | O(1) |
| Delete at end | O(n)* | O(1) |
| Delete in middle | O(n) | O(n) |

\* O(1) if we maintain a tail pointer