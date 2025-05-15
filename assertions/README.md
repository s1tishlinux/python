# Python Assertions

This folder contains comprehensive learning materials about Python's `assert` statement.

## Contents

1. **[demo.py](./demo.py)** - Complete tutorial with examples covering:
   - Basic assertion syntax
   - Using assertions for validation
   - Debugging with assertions
   - Assertions vs exceptions
   - Testing with assertions
   - Advanced assertion techniques
   - Best practices

2. **[lecture_outline.md](./lecture_outline.md)** - Structured presentation plan

3. **[slides.md](./slides.md)** - Ready-to-use slide content for presentations

4. **[exercises.py](./exercises.py)** - Practice exercises with solutions:
   - Basic assertions
   - Function validation
   - Class invariants
   - Data processing

5. **[real_world.py](./real_world.py)** - Practical applications in:
   - Data science
   - Web development
   - API development
   - Game development

6. **[cheatsheet.md](./cheatsheet.md)** - Quick reference guide for assertions

## Key Concepts

- Assertions are debugging aids that test a condition
- If the condition is True, execution continues silently
- If the condition is False, an AssertionError is raised
- Assertions can include optional error messages
- Assertions can be disabled in production with the -O flag

## When to Use Assertions

- Verifying function preconditions and postconditions
- Checking internal invariants
- Validating assumptions during development
- Simple testing

## When NOT to Use Assertions

- Data validation in production code
- Handling expected runtime errors
- Code with side effects
- Checking user inputs