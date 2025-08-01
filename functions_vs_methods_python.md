# 📘 Functions vs Methods in Python (Professional Reference)

Understanding the difference between **functions** and **methods** in Python is important to
avoid confusion when working with modules, objects, and OOP.

---

## ✅ 1. Definitions

### 🔹 Function
- A **standalone block of code** that performs a specific task.
- **Not tied to any class or object**.
- Called directly using the **module or global name**.

Example:

```python
import os
os.listdir('.')      # listdir is a **function** in the os module
```

Here:
- `listdir` exists in the **os module namespace**.
- It works independently of any specific object instance.

---

### 🔹 Method
- A **function defined inside a class**.
- **Belongs to an object** (instance of a class).
- **Can access and modify the object’s state**.
- Always has `self` as its first argument (implicitly passed).

Example:

```python
text = "hello"
print(text.upper())   # upper is a **method** of str objects
```

Here:
- `"hello"` is a `str` **object**.
- `.upper()` is **attached to this object** and knows how to operate on it.

---

## ✅ 2. Why `os` Module Has Functions (Not Methods)

- `os` is a **module**, not an object.
- Functions like `os.mkdir()` or `os.listdir()` do **one-off actions**, directly calling the OS kernel.
- They don’t need to store or remember any **internal state**, hence **functions** are sufficient.

Example:

```python
import os
os.mkdir("folder")   # Function just sends a system call to the OS
```

---

## ✅ 3. When Similar Actions Are Methods (Object-Oriented Style)

Python’s `pathlib` module introduces objects to represent filesystem paths.  
Here, the same operations become **methods** because they are now **behaviors of a Path object**.

Example:

```python
from pathlib import Path

path = Path("folder")
path.mkdir()         # mkdir is now a **method** tied to 'path' object
```

---

## ✅ 4. Difference Table

| **Aspect**     | **Function**                                     | **Method**                                     |
|-----------------|-------------------------------------------------|------------------------------------------------|
| **Defined in**  | Module or standalone script                     | Inside a class                                 |
| **Called on**   | Module name or directly                        | Object instance                                |
| **Access state**| No                                              | Yes (accesses object's attributes via `self`) |
| **Example**     | `os.listdir('.')`                              | `"hello".upper()`                             |

---

## ✅ 5. Easy Analogy

- **Function:** A **public telephone booth** – anyone can use it, no owner.  
- **Method:** A **private phone in your house** – it belongs to you (the object) and uses your personal connection (object data).

---

📌 **Key Takeaway:**  
- **Function = independent task.**  
- **Method = task tied to an object.**  
- Modules like `os` expose **functions** because they do not need object state.  
- Object-oriented libraries (e.g., `pathlib`) expose **methods** to work with specific objects.

