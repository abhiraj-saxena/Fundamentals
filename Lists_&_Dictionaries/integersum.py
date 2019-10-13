
# TODO: find the sum of the digits in a number
"""
import math


number = 1234567
numbertotal = 0
while number != 0:
    numberOnes = number % 10
    number = math.floor(number/10)
    numbertotal = numbertotal + numberOnes
print(numbertotal)

"""



# TODO: find the nth number in fibonacci sequence

#~ make fibonacci sequence
#~ 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci(n):
    firstInt = 1
    secondInt = 1
    i = -1

    fibonaccilist = [1]

    while i < n:
        nextInt = firstInt + secondInt
        firstInt = secondInt
        secondInt = nextInt
        fibonaccilist.append(nextInt)
        i = i+1
    print(fibonaccilist[i])



fibonacci(1)
"""
"""
finalresult = 0
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))
"""


# TODO find max number in a list using recursive formula

theList = [4, 3, 233, 6, 45, 432, 65, 87]

def maxList(n, numberlist):
    if n >= len(numberlist):
        return None
    elif n < len(numberlist):
        if numberlist[n] > numberlist[n-1]:
            maxList(n, numberlist)
            return numberlist[n]

        if numberlist[n] <= numberlist[n-1]:
            maxList(n, numberlist)

            return numberlist[n-1]
    
        
print(maxList(4, theList))

#         if theList[i] > theList[i-1]:
#         return theList[i]  
    
#     # elif theList[i] <= theList[i-1]:
#     #     x = theList[i-1] 

#     maxList(i)
# maxList(i)
# print(theList[i])
