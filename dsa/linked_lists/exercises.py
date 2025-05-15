#!/usr/bin/env python3
"""
Exercises for linked list implementations.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return "[" + " -> ".join(elements) + "]"


# Exercise 1: Reverse a linked list
def reverse_linked_list(head):
    """
    Reverse a singly linked list.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        New head of the reversed linked list
    """
    # Your solution here
    pass


# Exercise 2: Detect cycle in a linked list
def has_cycle(head):
    """
    Detect if a linked list has a cycle.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        True if the linked list has a cycle, False otherwise
    """
    # Your solution here
    pass


# Exercise 3: Find the middle node of a linked list
def find_middle_node(head):
    """
    Find the middle node of a linked list.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        The middle node of the linked list
    """
    # Your solution here
    pass


# Exercise 4: Remove nth node from end of list
def remove_nth_from_end(head, n):
    """
    Remove the nth node from the end of the linked list.
    
    Args:
        head: Head node of the linked list
        n: Position from the end to remove (1-based)
        
    Returns:
        New head of the linked list after removal
    """
    # Your solution here
    pass


# Exercise 5: Merge two sorted linked lists
def merge_two_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists into one sorted linked list.
    
    Args:
        l1: Head of first sorted linked list
        l2: Head of second sorted linked list
        
    Returns:
        Head of merged sorted linked list
    """
    # Your solution here
    pass


# Exercise 6: Remove duplicates from sorted list
def delete_duplicates(head):
    """
    Remove duplicates from a sorted linked list.
    
    Args:
        head: Head node of the sorted linked list
        
    Returns:
        Head of the linked list with duplicates removed
    """
    # Your solution here
    pass


# Exercise 7: Check if linked list is palindrome
def is_palindrome(head):
    """
    Check if a linked list is a palindrome.
    
    Args:
        head: Head node of the linked list
        
    Returns:
        True if the linked list is a palindrome, False otherwise
    """
    # Your solution here
    pass


# Exercise 8: Intersection of two linked lists
def get_intersection_node(headA, headB):
    """
    Find the node at which two linked lists intersect.
    
    Args:
        headA: Head of first linked list
        headB: Head of second linked list
        
    Returns:
        Intersection node or None if no intersection
    """
    # Your solution here
    pass


# Solutions

def reverse_linked_list_solution(head):
    """Solution for Exercise 1."""
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def has_cycle_solution(head):
    """Solution for Exercise 2."""
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


def find_middle_node_solution(head):
    """Solution for Exercise 3."""
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def remove_nth_from_end_solution(head, n):
    """Solution for Exercise 4."""
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


def merge_two_sorted_lists_solution(l1, l2):
    """Solution for Exercise 5."""
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


def delete_duplicates_solution(head):
    """Solution for Exercise 6."""
    if not head:
        return None
    
    current = head
    
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


def is_palindrome_solution(head):
    """Solution for Exercise 7."""
    if not head or not head.next:
        return True
    
    # Find the middle of the linked list
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half
    second_half = reverse_linked_list_solution(slow.next)
    
    # Compare first and second half
    first_half = head
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True


def get_intersection_node_solution(headA, headB):
    """Solution for Exercise 8."""
    if not headA or not headB:
        return None
    
    ptrA = headA
    ptrB = headB
    
    while ptrA != ptrB:
        # When ptrA reaches the end, redirect to headB
        ptrA = headB if ptrA is None else ptrA.next
        
        # When ptrB reaches the end, redirect to headA
        ptrB = headA if ptrB is None else ptrB.next
    
    return ptrA  # Either intersection node or None


if __name__ == "__main__":
    # Test Exercise 1: Reverse a linked list
    print("Testing Exercise 1: Reverse a linked list")
    llist = SinglyLinkedList()
    for i in range(1, 6):
        llist.append(i)
    
    print(f"Original list: {llist.print_list()}")
    llist.head = reverse_linked_list_solution(llist.head)
    print(f"Reversed list: {llist.print_list()}")
    
    # Test Exercise 2: Detect cycle
    print("\nTesting Exercise 2: Detect cycle")
    llist = SinglyLinkedList()
    for i in range(1, 6):
        llist.append(i)
    
    print(f"List without cycle: {llist.print_list()}")
    print(f"Has cycle: {has_cycle_solution(llist.head)}")
    
    # Create a cycle for testing
    current = llist.head
    while current.next:
        current = current.next
    current.next = llist.head.next  # Create cycle
    
    print("Created a cycle in the list")
    print(f"Has cycle: {has_cycle_solution(llist.head)}")
    
    # Test other exercises as needed