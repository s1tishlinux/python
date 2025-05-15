# Arrays and Lists in Python

Arrays and lists are fundamental data structures that store collections of elements in a sequential manner.

## Python Lists

In Python, the built-in `list` type is a dynamic array implementation that automatically resizes as elements are added or removed.

### Key Characteristics

- **Dynamic sizing**: Automatically grows and shrinks
- **Heterogeneous elements**: Can store different data types
- **Indexed access**: O(1) time complexity
- **Ordered collection**: Maintains insertion order
- **Mutable**: Can be modified after creation

### Basic Operations and Time Complexity

| Operation | Description | Time Complexity |
|-----------|-------------|----------------|
| Access | Retrieve element at index | O(1) |
| Search | Find element in unsorted list | O(n) |
| Insert (end) | Add element to end | O(1) amortized |
| Insert (middle) | Add element at specific position | O(n) |
| Delete (end) | Remove last element | O(1) |
| Delete (middle) | Remove element at specific position | O(n) |
| Length | Get number of elements | O(1) |

### Memory Layout

Python lists are implemented as arrays of references to objects:

```
List: [ptr1, ptr2, ptr3, ...]
       |     |     |
       v     v     v
      obj1  obj2  obj3
```

This allows for:
- Constant-time indexed access
- Storage of different object types
- Dynamic resizing (typically doubles in size when capacity is reached)

## Common List Operations

```python
# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Accessing elements
first = numbers[0]       # 1
last = numbers[-1]       # 5

# Slicing
subset = numbers[1:3]    # [2, 3]
reversed_list = numbers[::-1]  # [5, 4, 3, 2, 1]

# Adding elements
numbers.append(6)        # [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6]
numbers.extend([7, 8])   # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Removing elements
numbers.pop()            # Removes and returns last element
numbers.pop(0)           # Removes and returns first element
numbers.remove(5)        # Removes first occurrence of 5
del numbers[1]           # Removes element at index 1

# Finding elements
index = numbers.index(3)  # Returns index of first occurrence of 3
count = numbers.count(2)  # Counts occurrences of 2
exists = 4 in numbers     # True if 4 exists in the list

# Sorting
numbers.sort()           # In-place sort
numbers.sort(reverse=True)  # In-place sort in descending order
sorted_numbers = sorted(numbers)  # Returns new sorted list
```

## List Comprehensions

List comprehensions provide a concise way to create lists:

```python
# Basic list comprehension
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

## Arrays vs Lists

Python also offers the `array` module for more memory-efficient arrays of uniform data types:

```python
import array

# Create an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])
```

### When to use arrays vs lists:

- **Use lists when**:
  - You need a dynamic collection of heterogeneous objects
  - You need flexibility and built-in methods
  - Memory efficiency is not critical

- **Use arrays when**:
  - You need a collection of uniform data types
  - Memory efficiency is important
  - You're working with large numerical data

## NumPy Arrays

For numerical computing, NumPy arrays are more efficient than Python lists:

```python
import numpy as np

# Create a NumPy array
np_array = np.array([1, 2, 3, 4, 5])

# Vectorized operations
squared = np_array ** 2  # [1, 4, 9, 16, 25]
```

NumPy arrays offer:
- Vectorized operations (faster than loops)
- Memory efficiency
- Rich mathematical functions
- Multi-dimensional arrays

## Common List Algorithms

### Linear Search
```python
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1
```

### Binary Search (on sorted lists)
```python
def binary_search(arr, target):
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
```

### Two-Pointer Technique
```python
def reverse_list(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

## Best Practices

1. **Choose the right tool**: Lists for flexibility, arrays for numerical operations
2. **Avoid expensive operations**: Minimize insertions/deletions in the middle of large lists
3. **Use list comprehensions**: More readable and often faster than loops
4. **Consider memory**: For large datasets, use specialized data structures
5. **Leverage built-in functions**: `map()`, `filter()`, `sorted()`, etc.