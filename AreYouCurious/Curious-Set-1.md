# 1) `if __name__ == "__main__":` Explained

## What it does

- `__name__` is a special Python variable.
- When you run a Python file directly, `__name__` is set to `"__main__"`.
- When you import that file into another, `__name__` is set to the module's name.
- The line `if __name__ == "__main__":` means "Run the following code only if this file is executed directly."

## Why it matters

- Without this check, **all top-level code runs on import**, causing unwanted side effects.
- With this check, you can write code that is safe to import without running immediately.
- It helps organize your code so functions and classes can be reused without running test or demo code.

## Example without the check

```python
def run():
    print("Hello!")

print("This runs always!")
run()
```

- Running this file directly prints:
  ```
  This runs always!
  Hello!
  ```
- Importing this file in another will also print the above immediately (usually unwanted).

## Example with the check

```python
def run():
    print("Hello!")

if __name__ == "__main__":
    print("This runs only when executed directly!")
    run()
```

- Running this file directly prints:
  ```
  This runs only when executed directly!
  Hello!
  ```
- Importing this file in another will print nothing automatically.

## Summary Table

| Scenario                      | Without Check                        | With Check                                |
|-------------------------------|-------------------------------------|-------------------------------------------|
| Run file directly              | Runs all code                       | Runs code inside `if __name__ == "__main__"` only |
| Import file in another script  | Runs all top-level code immediately | Imports only definitions, no immediate code execution |



# 2) Understanding Default Arguments and Parameter Ordering in Python Functions

## The Rule About Default Arguments

- In Python, **default arguments apply only when you omit arguments from the end of the argument list**.
- Arguments are assigned to parameters **from left to right** based on position.
- If you provide fewer arguments than parameters, Python fills the parameters in order, starting from the first.

## Why Parameter Order Matters

Consider this function:

```python
def numbersViaRecursion(max=10, num=1):
    # function body
```

- `max` is the **first parameter** with a default value.
- `num` is the **second parameter** with a default value.

If you call:

```python
numbersViaRecursion(num + 1)
```

- Python treats the single argument as the **first parameter** (`max`), not the second (`num`).
- So `max` changes unexpectedly.
- `num` is not passed and falls back to its default (`1`), causing logic errors.

---

## Correct Usage Patterns

### Option 1: Reorder Parameters

```python
def numbersViaRecursion(num=1, max=10):
    # function body
```

- Now `num` comes first (the changing argument).
- Calling `numbersViaRecursion(num + 1)` works as expected.
- `max` uses its default value unless explicitly provided.

### Option 2: Pass All Arguments Explicitly

```python
def numbersViaRecursion(max=10, num=1):
    # function body
    numbersViaRecursion(max, num + 1)
```

- Always pass both `max` and `num` when calling recursively.
- Keeps `max` constant as intended.

---

## Summary Table

| Situation                           | Behavior                                            |
|-----------------------------------|----------------------------------------------------|
| Default argument omitted at end   | Parameter uses default value                        |
| Fewer arguments provided at start | Arguments fill parameters from left to right       |
| Default argument in first position| Must pass explicitly or reorder parameters          |

---

## Why This Rule Exists

- Python function calls are designed to be intuitive: positional arguments fill parameters from left to right.
- Allowing skipping of non-trailing arguments would complicate the function call syntax and readability.
- This design encourages consistent, clear calls and helps avoid ambiguity.

---

## Practical Tip

- Always **put parameters with default values at the end of your parameter list**.
- This makes your functions easier to call and reduces bugs related to argument passing.

---
