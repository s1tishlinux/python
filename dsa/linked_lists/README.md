# Linked Lists

A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.

## Types of Linked Lists

1. **Singly Linked List**: Each node has data and a reference to the next node
2. **Doubly Linked List**: Each node has data and references to both next and previous nodes
3. **Circular Linked List**: Last node points back to the first node (can be singly or doubly linked)

## Basic Structure

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

## Operations and Time Complexity

| Operation | Singly Linked List | Doubly Linked List |
|-----------|-------------------|-------------------|
| Access | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at beginning | O(1) | O(1) |
| Insert at end | O(n)* | O(1)** |
| Insert in middle | O(n) | O(n) |
| Delete at beginning | O(1) | O(1) |
| Delete at end | O(n)* | O(1)** |
| Delete in middle | O(n) | O(n) |

\* O(1) if we maintain a tail pointer  
\** Assuming we maintain a tail pointer

## Advantages of Linked Lists

1. **Dynamic Size**: Can grow or shrink during execution
2. **Efficient Insertions/Deletions**: Constant time at the beginning (and end with tail pointer)
3. **Memory Efficiency**: Only allocates memory as needed
4. **Implementation Flexibility**: Can easily implement stacks, queues, etc.

## Disadvantages of Linked Lists

1. **Random Access**: No direct access to elements by index (must traverse)
2. **Extra Memory**: Requires extra memory for pointers
3. **Cache Performance**: Poor locality of reference compared to arrays
4. **Reverse Traversal**: Difficult in singly linked lists

## Common Applications

1. **Dynamic Memory Allocation**
2. **Implementation of Stacks and Queues**
3. **Symbol Tables in Compiler Design**
4. **Undo Functionality in Applications**
5. **Hash Tables (for handling collisions)**
6. **Adjacency Lists for Graphs**

## Implementation Techniques

### Using a Dummy Head Node
- Simplifies edge cases by always having a node at the beginning
- Eliminates special cases for empty lists

### Using Tail Pointer
- Maintains a reference to the last node
- Enables O(1) insertions at the end

### Sentinel Nodes
- Special nodes at the beginning and/or end
- Simplifies boundary conditions

## Common Linked List Problems

1. **Detecting Cycles**: Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
2. **Finding the Middle**: Fast and slow pointers
3. **Reversing a Linked List**: Iterative and recursive approaches
4. **Merging Sorted Lists**: Used in merge sort implementation
5. **Detecting Intersection**: Finding where two lists join

## When to Use Linked Lists

- When frequent insertions and deletions are needed
- When the size of the data structure is unknown
- When memory is a concern and data size might vary significantly
- When random access is not required

## When to Avoid Linked Lists

- When frequent random access is needed
- When memory overhead is a concern
- When cache performance is critical