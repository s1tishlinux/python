# 📘 Python Pathlib Cheat Sheet (Tabular Professional Reference)

The `pathlib` module in Python provides an **object-oriented interface** for working with file system paths. 
It is a modern alternative to `os.path` with **methods bound to path objects** for cleaner and more readable code.

---

## ✅ Main Classes

| **Class**       | **Purpose** |
|-----------------|-------------|
| `Path`          | Represents a filesystem path (file or directory). |
| `PurePath`      | Path operations without accessing the actual filesystem (useful for parsing paths only). |
| `PosixPath`     | Path implementation for Linux/Mac (POSIX systems). |
| `WindowsPath`   | Path implementation for Windows systems. |

---

## ✅ Commonly Used Methods

| **Method / Property**   | **Purpose**                                      | **Usage Example**                                     |
|-------------------------|--------------------------------------------------|------------------------------------------------------|
| `Path.cwd()`            | Returns current working directory.               | `Path.cwd()`                                         |
| `Path.home()`           | Returns home directory of the user.              | `Path.home()`                                        |
| `path.exists()`         | Checks if the path exists.                       | `Path("file.txt").exists()`                          |
| `path.is_file()`        | Checks if the path is a file.                    | `Path("file.txt").is_file()`                         |
| `path.is_dir()`         | Checks if the path is a directory.               | `Path("folder").is_dir()`                            |
| `path.mkdir()`          | Creates a new directory.                         | `Path("new_folder").mkdir()`                         |
| `path.rmdir()`          | Removes an empty directory.                      | `Path("new_folder").rmdir()`                         |
| `path.unlink()`         | Deletes a file.                                  | `Path("file.txt").unlink()`                          |
| `path.rename()`         | Renames or moves a file/directory.               | `Path("old.txt").rename("new.txt")`                  |
| `path.iterdir()`        | Iterates over files in a directory.               | `for p in Path(".").iterdir(): print(p)`             |
| `path.glob("*.txt")`    | Finds files matching a pattern.                  | `list(Path(".").glob("*.txt"))`                      |
| `path.read_text()`      | Reads entire file content as string.             | `Path("file.txt").read_text()`                       |
| `path.write_text()`     | Writes text to a file (overwrites existing).     | `Path("file.txt").write_text("Hello World")`         |
| `path.read_bytes()`     | Reads entire file content as bytes.              | `Path("file.txt").read_bytes()`                      |
| `path.write_bytes()`    | Writes bytes to a file.                          | `Path("file.txt").write_bytes(b"data")`              |
| `path.parts`            | Returns path components as tuple.                | `Path("/usr/bin").parts` → `('/', 'usr', 'bin')`     |
| `path.name`             | Returns filename with extension.                  | `Path("file.txt").name`                              |
| `path.stem`             | Returns filename without extension.              | `Path("file.txt").stem`                              |
| `path.suffix`           | Returns file extension.                          | `Path("file.txt").suffix`                            |
| `path.parent`           | Returns the parent directory.                    | `Path("/home/user/file.txt").parent`                 |
| `path.joinpath()`       | Joins path components (alternative to `/`).      | `Path("folder").joinpath("file.txt")`                |
| `path.resolve()`        | Returns absolute path (resolving symlinks).      | `Path("file.txt").resolve()`                         |

---

## ✅ Example Usage

```python
from pathlib import Path

# Current directory
print(Path.cwd())

# Creating a file and reading it
file = Path("demo.txt")
file.write_text("Hello, pathlib!")
print(file.read_text())

# Iterating over files
for p in Path(".").glob("*.txt"):
    print("Found:", p.name)
```

---

## ✅ Professional Best Practices

| **Best Practice**                               | **Reason** |
|-------------------------------------------------|-------------|
| Prefer `pathlib` over `os.path`.                | Cleaner OOP syntax, more readable code. |
| Use `Path.home()` and `Path.cwd()` for safe paths. | Avoids hardcoding absolute paths. |
| Use `.exists()` before reading/deleting files.  | Prevents errors in file operations. |
| Use `.glob()` or `.iterdir()` for directory scans. | Better performance than manual string handling. |
| Use `.resolve()` to handle relative paths safely. | Ensures compatibility across OS platforms. |

---

📌 **Tip:** `pathlib` integrates seamlessly with many libraries (like `open()`) and is the **recommended modern approach** for handling filesystem paths in Python.
