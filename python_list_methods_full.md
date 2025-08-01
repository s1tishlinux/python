# 📜 Python List Methods – Complete Cheat Sheet

Python `list` objects have **two types of methods**:

1️⃣ **Special (Magic/Dunder) Methods** – used internally by Python to support operators and built-in functions.  
2️⃣ **Regular (User-facing) Methods** – commonly used in everyday programming.

---

## ✅ 1. Special (Magic/Dunder) Methods

These methods are automatically called by Python when you perform specific actions on a list.

| **Method**        | **Purpose / Triggered When** |
|--------------------|-----------------------------|
| `__add__`          | `list1 + list2` → concatenates lists. |
| `__mul__`, `__rmul__` | `list * 3` → repeats list elements. |
| `__getitem__`      | Accessing elements → `list[i]`. |
| `__setitem__`      | Modifying elements → `list[i] = value`. |
| `__delitem__`      | Deleting elements → `del list[i]`. |
| `__contains__`     | Checking membership → `x in list`. |
| `__len__`          | Using `len(list)`. |
| `__iter__`         | Iterating → `for x in list`. |
| `__eq__`, `__ne__`, `__lt__`, `__gt__`, `__le__`, `__ge__` | Comparison operators (`==`, `!=`, `<`, `>`...). |
| `__str__`, `__repr__` | String representation when printing. |
| `__class__`, `__doc__` | Metadata about the list class. |
| `__sizeof__`       | Returns memory size of list in bytes. |
| `__iadd__`         | `list += another_list`. |
| `__delattr__`, `__getattribute__`, `__setattr__` | Internal attribute handling (rarely used manually). |
| `__reduce__`, `__reduce_ex__` | Used in object serialization (pickling). |
| `__subclasshook__` | Used in class inheritance checks. |
| `__new__`, `__init__` | Object creation and initialization. |
| `__class_getitem__` | Supports type hints like `list[int]`. |

---

### 🔹 Examples of Special Methods

```python
nums = [1, 2, 3]
print(nums.__add__([4, 5]))    # [1, 2, 3, 4, 5]
print(nums.__getitem__(1))     # 2
nums.__setitem__(0, 10)        # [10, 2, 3]
print(nums.__contains__(3))    # True
print(nums.__len__())          # 3
```

---

## ✅ 2. Regular (User-facing) List Methods

These are the methods you **commonly use** to manipulate lists.

| **Method** | **Purpose** |
|------------|-------------|
| `append(x)` | Adds a single element `x` to the end of the list. |
| `clear()` | Removes all elements from the list. |
| `copy()` | Returns a shallow copy of the list. |
| `count(x)` | Returns how many times `x` appears. |
| `extend(iterable)` | Adds all elements from another iterable. |
| `index(x[, start[, end]])` | Returns index of first occurrence of `x`. |
| `insert(i, x)` | Inserts `x` at position `i`. |
| `pop([i])` | Removes and returns element at index `i`. Default: last item. |
| `remove(x)` | Removes first occurrence of `x`. |
| `reverse()` | Reverses list in place. |
| `sort(key=None, reverse=False)` | Sorts list in place (ascending by default). |

---

### 🔹 Example Usage

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")      # ['apple', 'banana', 'cherry', 'mango']
fruits.extend(["grape"])    # ['apple', 'banana', 'cherry', 'mango', 'grape']
fruits.insert(1, "orange")  # ['apple', 'orange', 'banana', 'cherry', 'mango', 'grape']
fruits.remove("banana")     # ['apple', 'orange', 'cherry', 'mango', 'grape']
fruits.pop(2)               # removes 'cherry'
fruits.sort()               # ['apple', 'grape', 'mango', 'orange']
fruits.reverse()            # ['orange', 'mango', 'grape', 'apple']
```

---

## ✅ Quick Tip

To see **all available methods and attributes** for a list dynamically:

```python
print(dir(list))
```

---

📌 **Summary:**  
- Python lists have **11 user-facing methods**.  
- Other `__methods__` are special functions Python calls automatically to enable list behavior with operators and built-ins.
