#PseudoCode

# 1. Ask the user to enter a non-negative integer and store it as num
# 2. Initialize a variable factorial to 1
# 3. Use a loop from 1 to num (inclusive)
# 4. Multiply factorial by the current loop number each time
# 5. After the loop ends, print the factorial

num = int(input("Enter the number to calculate factorial: "))

def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

if __name__ == "__main__":
    # factorial(num)
    print(f"The factorial of {num} is {factorial(num)}")
    factorial(num)