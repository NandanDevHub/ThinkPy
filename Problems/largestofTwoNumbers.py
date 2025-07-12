#Psudo Code 
# 1. Ask the user to enter the first number and store it as num1
# 2. Ask the user to enter the second number and store it as num2
# 3. Compare num1 and num2
# 4. If num1 is greater than num2, print "num1 is greater"
# 5. Otherwise, print "num2 is greater or equal"

def largestOfTwoNumbers():
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        
        if (num1 > num2):
            print(f"{num1} is greater.")
        elif (num2 > num1):
            print(f"{num2} is greater.")
        else:
            print("Both numbers are equal.")
    except ValueError:
        print("Please enter valid numbers.")
        return
    
    if __name__ == "__main__":
        largestOfTwoNumbers()