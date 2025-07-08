# Understanding Lambda Functions in Python

## What is a Lambda Function?

- A **lambda function** is a small, anonymous (unnamed) function defined with the keyword `lambda`.
- It is used to create **simple functions in a single line** without the need for a full `def` block.
- Lambdas are often used for short, throwaway functions that are not reused elsewhere.

---

## Syntax

```python
lambda arguments: expression
```

- `arguments`: Input parameters to the function (can be zero or more).
- `expression`: A single expression that is evaluated and returned.

---

## Example: Normal function vs Lambda

### Normal function

```python
def add(x, y):
    return x + y

print(add(3, 5))  # Output: 8
```

### Lambda function equivalent

```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```

---

## Common Uses of Lambda Functions

- Used with functions like `map()`, `filter()`, and `sorted()` where a simple function is needed temporarily.

### Example with `map()`

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

### Example with `filter()`

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
```

---

## Why Use Lambdas?

- **Concise:** Write simple functions in a single line.
- **Anonymous:** No need to name a function you only use once.
- **Functional Programming:** Lambdas fit well with functions that take other functions as arguments.

---

## Limitations

- Lambdas can only contain **expressions**, not statements.
- They are less readable for complex functions — better to use `def` for those.

---

## Summary Table

| Aspect         | Explanation                          |
|----------------|------------------------------------|
| Syntax         | `lambda args: expression`           |
| Use case       | Short, one-off functions             |
| Common funcs   | Used with `map()`, `filter()`, etc. |
| Limitation     | Single expression, no complex logic |

---
