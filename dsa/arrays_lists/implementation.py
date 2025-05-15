#!/usr/bin/env python3
"""
Implementation of common array/list operations and algorithms in Python.
"""

class DynamicArray:
    """
    A simple implementation of a dynamic array to demonstrate how Python lists work internally.
    This is for educational purposes - in practice, use Python's built-in list.
    """
    
    def __init__(self):
        """Initialize an empty array with capacity 1."""
        self.capacity = 1
        self.length = 0
        self.array = self._create_array(self.capacity)
    
    def _create_array(self, capacity):
        """Create a new array with given capacity."""
        return [None] * capacity
    
    def __len__(self):
        """Return the number of elements in the array."""
        return self.length
    
    def __getitem__(self, index):
        """Get item at index."""
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        return self.array[index]
    
    def __setitem__(self, index, value):
        """Set item at index to value."""
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        self.array[index] = value
    
    def append(self, value):
        """Add an element to the end of the array."""
        if self.length == self.capacity:
            self._resize(2 * self.capacity)  # Double the capacity
        
        self.array[self.length] = value
        self.length += 1
    
    def _resize(self, new_capacity):
        """Resize the array to the new capacity."""
        new_array = self._create_array(new_capacity)
        
        # Copy existing elements
        for i in range(self.length):
            new_array[i] = self.array[i]
        
        self.array = new_array
        self.capacity = new_capacity
    
    def insert(self, index, value):
        """Insert value at index, shifting elements if necessary."""
        if not 0 <= index <= self.length:
            raise IndexError("Index out of range")
        
        # If array is full, resize
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        
        # Shift elements to make room
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1]
        
        self.array[index] = value
        self.length += 1
    
    def remove(self, index):
        """Remove element at index, shifting elements if necessary."""
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        
        # Shift elements to fill the gap
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i+1]
        
        self.array[self.length - 1] = None
        self.length -= 1
        
        # If array is less than 1/4 full, resize to half
        if 0 < self.length < self.capacity // 4:
            self._resize(self.capacity // 2)
    
    def __str__(self):
        """Return string representation of the array."""
        return str([self.array[i] for i in range(self.length)])


def linear_search(arr, target):
    """
    Search for target in arr using linear search.
    
    Args:
        arr: List or array to search in
        target: Element to search for
        
    Returns:
        Index of target if found, -1 otherwise
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Search for target in sorted arr using binary search.
    
    Args:
        arr: Sorted list or array to search in
        target: Element to search for
        
    Returns:
        Index of target if found, -1 otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=None, right=None):
    """
    Search for target in sorted arr using recursive binary search.
    
    Args:
        arr: Sorted list or array to search in
        target: Element to search for
        left: Start index (default: 0)
        right: End index (default: len(arr)-1)
        
    Returns:
        Index of target if found, -1 otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def two_sum(arr, target):
    """
    Find two numbers in arr that add up to target.
    
    Args:
        arr: List of numbers
        target: Target sum
        
    Returns:
        Tuple of indices of the two numbers, or None if not found
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}  # Value -> index mapping
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    
    return None


def reverse_array(arr):
    """
    Reverse an array in-place.
    
    Args:
        arr: Array to reverse
        
    Returns:
        The reversed array (same object)
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr


def rotate_array(arr, k):
    """
    Rotate array to the right by k steps.
    
    Args:
        arr: Array to rotate
        k: Number of steps to rotate
        
    Returns:
        The rotated array (same object)
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    k = k % n  # Handle case where k > n
    
    # Reverse the entire array
    reverse_array(arr)
    
    # Reverse first k elements
    reverse_array(arr[:k])
    
    # Reverse remaining elements
    reverse_array(arr[k:])
    
    return arr


def remove_duplicates(arr):
    """
    Remove duplicates from a sorted array in-place.
    
    Args:
        arr: Sorted array
        
    Returns:
        Length of the array after removing duplicates
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0
    
    # i is the index where unique elements should be placed
    i = 0
    
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1  # Length of unique elements


def max_subarray_sum(arr):
    """
    Find the contiguous subarray with the largest sum.
    
    Args:
        arr: Array of integers
        
    Returns:
        Maximum sum
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0
    
    current_sum = max_sum = arr[0]
    
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


if __name__ == "__main__":
    # Test DynamicArray
    print("Testing DynamicArray...")
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
    print(f"Array: {arr}")
    
    arr.insert(5, 99)
    print(f"After inserting 99 at index 5: {arr}")
    
    arr.remove(5)
    print(f"After removing element at index 5: {arr}")
    
    # Test search algorithms
    print("\nTesting search algorithms...")
    test_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    
    linear_result = linear_search(test_arr, target)
    print(f"Linear search for {target}: found at index {linear_result}")
    
    binary_result = binary_search(test_arr, target)
    print(f"Binary search for {target}: found at index {binary_result}")
    
    # Test array operations
    print("\nTesting array operations...")
    test_arr = [1, 2, 3, 4, 5]
    print(f"Original array: {test_arr}")
    
    reversed_arr = reverse_array(test_arr.copy())
    print(f"Reversed array: {reversed_arr}")
    
    rotated_arr = rotate_array(test_arr.copy(), 2)
    print(f"Array rotated by 2: {rotated_arr}")
    
    # Test two sum
    print("\nTesting two sum...")
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Two sum for target {target}: indices {result}")
    
    # Test max subarray sum
    print("\nTesting max subarray sum...")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(nums)
    print(f"Max subarray sum: {result}")