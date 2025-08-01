# 📘 Python Dotenv Cheat Sheet (Tabular Professional Reference)

This cheat sheet summarizes the **key methods** in the `python-dotenv` library in a **tabular format**, 
including their purpose, usage, and professional notes.

---

## ✅ Main Methods

| **Method**        | **Purpose**                                        | **Usage Example**                                           | **Professional Notes** |
|--------------------|----------------------------------------------------|------------------------------------------------------------|------------------------|
| `load_dotenv()`    | Load all variables from `.env` into `os.environ`.  | `load_dotenv(dotenv_path=".env", override=True)`           | Use once at app startup to initialize environment variables. |
| `get_key()`        | Fetch value of a single key from `.env`.           | `get_key(".env", "API_KEY")`                              | Ideal for reading one variable without modifying global env. |
| `set_key()`        | Add or update a variable in `.env`.                | `set_key(".env", "NEW_KEY", "value")`                     | Useful in setup scripts or CI/CD pipelines to generate `.env`. |
| `unset_key()`      | Remove a specific variable from `.env`.            | `unset_key(".env", "OLD_KEY")`                            | Cleans up unused or sensitive keys dynamically. |
| `dotenv_values()`  | Load `.env` into a **dictionary** only.            | `dotenv_values(".env")`                                   | Does not modify `os.environ`, safe for temporary config reads. |
| `find_dotenv()`    | Auto-search `.env` file in parent directories.     | `find_dotenv()`                                           | Helps locate `.env` in large project structures automatically. |

---

## ✅ Example `.env` File

```
DB_HOST=localhost
DB_USER=admin
DB_PASS=secret
DEBUG=True
```

---

## ✅ Example Code

```python
from dotenv import load_dotenv, get_key, set_key, unset_key, dotenv_values, find_dotenv
import os

# Load all environment variables
load_dotenv()

# Get one variable
api_key = get_key(".env", "API_KEY")

# Add a new variable
set_key(".env", "NEW_KEY", "new_value")

# Remove a variable
unset_key(".env", "OLD_KEY")

# Load as dictionary
config = dotenv_values(find_dotenv())
print(config["DB_USER"])

# Access loaded environment variable
print(os.getenv("DB_HOST"))
```

---

## ✅ Professional Best Practices

| **Best Practice** | **Reason** |
|-------------------|------------|
| Keep secrets out of source code. | Prevent accidental leaks in Git repositories. |
| Use `.env.example` for sharing variable names. | Team members know required variables without exposing secrets. |
| Load variables once at startup. | Avoid unnecessary re-reads and overrides. |
| Manually convert values to proper types. | Environment variables are always strings. |
| Use `find_dotenv()` for large projects. | Ensures `.env` is found even in nested folders. |

---

📌 **Tip:** `dotenv` is widely used in professional software engineering to build **secure, portable, and configurable applications**.
