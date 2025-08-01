# 📘 Python Dotenv Cheat Sheet (Professional Reference)

This cheat sheet summarizes the **key methods** in the `python-dotenv` library, 
how they work internally, and why professionals use them to write clean, secure code.

---

## ✅ 1. What is dotenv?

- `.env` file = Simple text file for **environment variables**:
```
KEY1=value1
KEY2=value2
```
- Used to keep **secrets and configuration** outside the source code.
- Python loads these values into **`os.environ`** at runtime.

---

## ✅ 2. Main Methods in `python-dotenv`

### 🔹 1) `load_dotenv()`
- **Purpose:** Load all variables from `.env` into `os.environ`.
- **Usage:**
```python
from dotenv import load_dotenv
load_dotenv()  # Default: loads .env from current directory
```
- **Parameters:**
  - `dotenv_path`: specify a file path
  - `override`: `True` to overwrite existing variables

---

### 🔹 2) `get_key()`
- **Purpose:** Get the value of a single key from `.env` without loading all.
- **Usage:**
```python
from dotenv import get_key
value = get_key(".env", "API_KEY")
```

---

### 🔹 3) `set_key()`
- **Purpose:** Add or update a variable in `.env` file programmatically.
- **Usage:**
```python
from dotenv import set_key
set_key(".env", "NEW_KEY", "new_value")
```

---

### 🔹 4) `unset_key()`
- **Purpose:** Remove a key from `.env`.
- **Usage:**
```python
from dotenv import unset_key
unset_key(".env", "OLD_KEY")
```

---

## ✅ 3. Supporting Functions

| **Function**      | **Purpose** |
|--------------------|-------------|
| `dotenv_values()`  | Loads `.env` as a **dictionary** without changing `os.environ`. |
| `find_dotenv()`    | Searches for `.env` **up the folder hierarchy**. |

Example:
```python
from dotenv import dotenv_values, find_dotenv
config = dotenv_values(find_dotenv())
print(config["DB_USER"])
```

---

## ✅ 4. Professional Best Practices

1. Keep secrets **out of source code**.
2. Use **`.env.example`** (no secrets) to share required variables with team.
3. Load variables **once** at application startup.
4. Use `get_key()` when you only need one value (less memory usage).
5. Use `set_key()` in **setup scripts or CI/CD pipelines** to generate `.env` dynamically.
6. Convert values manually (all env values are strings):
```python
debug_mode = os.getenv("DEBUG", "False").lower() == "true"
```

---

## ✅ 5. Process Flow (Behind the Scenes)

1. Python script calls `load_dotenv()`.
2. Reads `.env` line by line → key-value pairs.
3. Adds them to **process environment table (`os.environ`)**.
4. Your code accesses them via:
```python
import os
print(os.getenv("API_KEY"))
```

---

## ✅ Quick Summary Table

| **Method**        | **Purpose**                                |
|--------------------|--------------------------------------------|
| `load_dotenv()`    | Load all variables into `os.environ`.      |
| `get_key()`        | Get one variable from `.env` file.         |
| `set_key()`        | Add or update variable in `.env`.          |
| `unset_key()`      | Remove variable from `.env`.               |
| `dotenv_values()`  | Load `.env` as a dictionary only.          |
| `find_dotenv()`    | Locate `.env` file automatically.          |

---

📌 **Tip:** `dotenv` makes your code **secure, portable, and configurable**.  
It follows **12-Factor App principles**, used in professional software engineering.

