# Space Complexity Analysis

Space complexity measures the amount of memory an algorithm uses relative to the input size.

## Understanding Space Complexity

Space complexity includes:
1. **Input space**: Memory needed to store the input
2. **Auxiliary space**: Extra memory used by the algorithm (excluding input)
3. **Total space**: Input space + Auxiliary space

When discussing space complexity, we typically focus on auxiliary space.

## Common Space Complexities

### O(1) - Constant Space
- Uses a fixed amount of memory regardless of input size
- Examples: Simple variables, fixed-size data structures

```python
def find_max(arr):
    max_val = float('-inf')  # O(1) space
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```

### O(n) - Linear Space
- Memory usage grows linearly with input size
- Examples: Creating a new array of size n

```python
def duplicate_array(arr):
    duplicate = []  # O(n) space
    for item in arr:
        duplicate.append(item)
    return duplicate
```

### O(n²) - Quadratic Space
- Memory usage grows quadratically with input size
- Examples: 2D matrices, adjacency matrices for graphs

```python
def create_matrix(n):
    matrix = []  # O(n²) space
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        matrix.append(row)
    return matrix
```

### O(log n) - Logarithmic Space
- Memory usage grows logarithmically with input size
- Examples: Recursive binary search (call stack)

```python
def binary_search_recursive(arr, target, left, right):
    # O(log n) space due to recursive call stack
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

## Space Complexity in Recursion

Recursive algorithms use the call stack, which contributes to space complexity:

1. **Tail Recursion**: When the recursive call is the last operation
   - Some languages optimize this to O(1) space (Python doesn't)

2. **Non-Tail Recursion**: When operations occur after the recursive call
   - Typically uses O(n) or O(log n) space depending on recursion depth

```python
# O(n) space due to n recursive calls on stack
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)  # Not tail recursive

# Could be O(1) space with tail recursion optimization
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n-1, n * accumulator)  # Tail recursive
```

## In-Place Algorithms

In-place algorithms transform data with minimal auxiliary space (typically O(1)):

```python
def reverse_in_place(arr):
    # O(1) auxiliary space
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

## Space-Time Tradeoffs

Often, reducing time complexity requires increasing space complexity and vice versa:

1. **Memoization**: Trades space for time
   ```python
   def fibonacci_memoized(n, memo={}):
       if n in memo:
           return memo[n]
       if n <= 1:
           return n
       memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
       return memo[n]
   ```

2. **Recomputation**: Trades time for space
   ```python
   def fibonacci_recompute(n):
       if n <= 1:
           return n
       return fibonacci_recompute(n-1) + fibonacci_recompute(n-2)
   ```

## Tips for Optimizing Space Complexity

1. **Use in-place operations** when possible
2. **Reuse variables** instead of creating new ones
3. **Consider iterative solutions** instead of recursive ones
4. **Use generators** for large sequences instead of storing all values
5. **Be mindful of hidden space costs** like string concatenation in loops