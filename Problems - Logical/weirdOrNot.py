def weird(n):
    if n % 2 != 0:
        print("Weird")
    elif  2 <= n <= 5: # Checking if n is in the range 2 to 5
        print("Not Weird")
    elif 6 <= n <= 20: # Checking if n is in the range 6 to 20
        print("Weird")
    else:
        print("Not Weird")


if __name__ == '__main__':
    n = int(input("Enter the Number:").strip())
    weird(n)
