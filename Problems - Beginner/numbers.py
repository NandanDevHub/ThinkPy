def numbersViaRange():
    for num in range(1, 10):
        print(num)
        
def numbersViaManual():
    num = 1
    while num < 5:
        print(num)
        num = num + 1
        
def numbersViaRecursion(num=1, max=15):
    if num > max:
     return

    print (num)
    numbersViaRecursion(num + 1)
    
def numbersViaMap():
    list(map(lambda x: print(x), range(1,13)))
        
if __name__ == "__main__":
  numbersViaRange()
  print ("----")
  numbersViaManual()
  print ("----")
  numbersViaRecursion()
  print ("----")
  numbersViaMap()
    