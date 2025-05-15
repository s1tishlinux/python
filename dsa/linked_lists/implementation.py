#!/usr/bin/env python3
"""
Implementation of linked list data structures.
"""

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"


class DoublyNode:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return f"DoublyNode({self.data})"


class SinglyLinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None
    
    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
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
        """Insert a new node at the specified position."""
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
        """Delete the node at the beginning of the list."""
        if self.is_empty():
            raise Exception("List is empty")
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def delete_at_end(self):
        """Delete the node at the end of the list."""
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
        """Delete the node at the specified position."""
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
        """Search for a node with the specified data."""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1  # Not found
    
    def get(self, position):
        """Get the data at the specified position."""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def has_cycle(self):
        """Detect if the linked list has a cycle using Floyd's algorithm."""
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
    
    def find_middle(self):
        """Find the middle node of the linked list."""
        if not self.head:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def __len__(self):
        """Return the size of the linked list."""
        return self.size
    
    def __str__(self):
        """Return a string representation of the linked list."""
        if self.is_empty():
            return "[]"
        
        result = []
        current = self.head
        
        while current:
            result.append(str(current.data))
            current = current.next
        
        return "[" + " -> ".join(result) + "]"


class DoublyLinkedList:
    """Doubly linked list implementation."""
    
    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None
    
    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = DoublyNode(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = DoublyNode(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def insert_at_position(self, data, position):
        """Insert a new node at the specified position."""
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        if position == self.size:
            self.insert_at_end(data)
            return
        
        new_node = DoublyNode(data)
        current = self.head
        
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        
        self.size += 1
    
    def delete_at_beginning(self):
        """Delete the node at the beginning of the list."""
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
        """Delete the node at the end of the list."""
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
    
    def delete_at_position(self, position):
        """Delete the node at the specified position."""
        if self.is_empty():
            raise Exception("List is empty")
        
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        if position == 0:
            return self.delete_at_beginning()
        
        if position == self.size - 1:
            return self.delete_at_end()
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        current.prev.next = current.next
        current.next.prev = current.prev
        
        data = current.data
        self.size -= 1
        return data
    
    def search(self, data):
        """Search for a node with the specified data."""
        current = self.head
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1  # Not found
    
    def get(self, position):
        """Get the data at the specified position."""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        
        if position < self.size // 2:
            # Start from head
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            # Start from tail
            current = self.tail
            for _ in range(self.size - 1 - position):
                current = current.prev
        
        return current.data
    
    def reverse(self):
        """Reverse the doubly linked list in-place."""
        if self.is_empty() or self.head == self.tail:
            return
        
        current = self.head
        self.tail = current
        
        while current:
            # Swap next and prev pointers
            temp = current.next
            current.next = current.prev
            current.prev = temp
            
            # Move to the next node (which is now current.prev)
            if not current.prev:
                self.head = current
            current = current.prev
    
    def __len__(self):
        """Return the size of the linked list."""
        return self.size
    
    def __str__(self):
        """Return a string representation of the linked list."""
        if self.is_empty():
            return "[]"
        
        result = []
        current = self.head
        
        while current:
            result.append(str(current.data))
            current = current.next
        
        return "[" + " <-> ".join(result) + "]"


def merge_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists into a new sorted list.
    
    Args:
        l1: Head of first sorted linked list
        l2: Head of second sorted linked list
        
    Returns:
        Head of merged sorted linked list
    """
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


if __name__ == "__main__":
    # Test Singly Linked List
    print("Testing Singly Linked List...")
    sll = SinglyLinkedList()
    
    sll.insert_at_beginning(3)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(1)
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    
    print(f"List: {sll}")
    print(f"Size: {len(sll)}")
    
    print(f"Element at position 2: {sll.get(2)}")
    print(f"Position of element 4: {sll.search(4)}")
    
    print(f"Deleting element at beginning: {sll.delete_at_beginning()}")
    print(f"List after deletion: {sll}")
    
    print(f"Deleting element at end: {sll.delete_at_end()}")
    print(f"List after deletion: {sll}")
    
    print(f"Deleting element at position 1: {sll.delete_at_position(1)}")
    print(f"List after deletion: {sll}")
    
    print("Reversing the list...")
    sll.reverse()
    print(f"Reversed list: {sll}")
    
    print(f"Middle element: {sll.find_middle()}")
    
    # Test Doubly Linked List
    print("\nTesting Doubly Linked List...")
    dll = DoublyLinkedList()
    
    dll.insert_at_beginning(3)
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(1)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    
    print(f"List: {dll}")
    print(f"Size: {len(dll)}")
    
    print(f"Element at position 2: {dll.get(2)}")
    print(f"Position of element 4: {dll.search(4)}")
    
    print(f"Deleting element at beginning: {dll.delete_at_beginning()}")
    print(f"List after deletion: {dll}")
    
    print(f"Deleting element at end: {dll.delete_at_end()}")
    print(f"List after deletion: {dll}")
    
    print(f"Deleting element at position 1: {dll.delete_at_position(1)}")
    print(f"List after deletion: {dll}")
    
    print("Reversing the list...")
    dll.reverse()
    print(f"Reversed list: {dll}")