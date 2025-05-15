# Time Complexity Analysis

Time complexity measures the computational efficiency of an algorithm in terms of the amount of time it takes to run as a function of the input size.

## Asymptotic Notations

### Big O Notation (O)
- Represents the **upper bound** of an algorithm's time complexity
- Describes the worst-case scenario
- Most commonly used notation
- Example: O(n²) means the algorithm's time complexity grows no faster than n²

### Theta Notation (Θ)
- Represents the **tight bound** of an algorithm's time complexity
- Describes the average-case scenario
- Example: Θ(n log n) means the algorithm's time complexity grows exactly at the rate of n log n

### Omega Notation (Ω)
- Represents the **lower bound** of an algorithm's time complexity
- Describes the best-case scenario
- Example: Ω(n) means the algorithm's time complexity grows at least as fast as n

## Common Time Complexities

Listed from most efficient to least efficient:

### O(1) - Constant Time
- Execution time is independent of input size
- Examples: Array access, hash table lookup (average case)

```python
def get_first_element(arr):
    return arr[0]  # O(1) - constant time operation
```

### O(log n) - Logarithmic Time
- Execution time grows logarithmically with input size
- Examples: Binary search, balanced binary search tree operations

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

### O(n) - Linear Time
- Execution time grows linearly with input size
- Examples: Linear search, traversing an array

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### O(n log n) - Linearithmic Time
- Execution time grows in proportion to n log n
- Examples: Efficient sorting algorithms (merge sort, heap sort, quicksort average case)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)
```

### O(n²) - Quadratic Time
- Execution time grows quadratically with input size
- Examples: Nested loops, bubble sort, insertion sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### O(2^n) - Exponential Time
- Execution time doubles with each addition to the input size
- Examples: Recursive algorithms solving problems of size n

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### O(n!) - Factorial Time
- Execution time grows factorially with input size
- Examples: Generating all permutations, brute force traveling salesman

```python
def permutations(arr):
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        for p in permutations(arr[:i] + arr[i+1:]):
            result.append([arr[i]] + p)
    
    return result
```

## Time Complexity Comparison

| Complexity | n=10 | n=100 | n=1000 |
|------------|------|-------|--------|
| O(1)       | 1    | 1     | 1      |
| O(log n)   | 3    | 7     | 10     |
| O(n)       | 10   | 100   | 1000   |
| O(n log n) | 30   | 700   | 10000  |
| O(n²)      | 100  | 10000 | 10^6   |
| O(2^n)     | 1024 | 10^30 | 10^301 |
| O(n!)      | 10^6 | 10^158| 10^2568|

## Tips for Analyzing Time Complexity

1. **Loops**: Each nested loop typically multiplies the complexity
   - Single loop: O(n)
   - Nested loop: O(n²)
   - Triple nested loop: O(n³)

2. **Recursive Functions**: Analyze the number of recursive calls and work per call
   - For divide and conquer algorithms: Often O(n log n)

3. **Sequence of Operations**: Add the complexities
   - O(n) + O(n²) = O(n²) (only the highest order term matters)

4. **Conditional Statements**: Consider the worst-case branch

5. **Logarithmic Complexity**: Often appears when the problem size is repeatedly divided (binary search, balanced trees)