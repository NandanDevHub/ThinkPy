# PseudoCode

# 1. Ask the user to enter a number and store it as num
# 2. If num is greater than 0, print "num is positive"
# 3. Else if num is less than 0, print "num is negative"
# 4. Else, print "num is zero"

def positiveOrNegative():
    num = float(input("Enter the number"))
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print("{num} is negative")
    else:
        print("Aryabhatta")
        
if __name__ == "__main__":
    positiveOrNegative()