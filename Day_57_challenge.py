#make a recursion that calculates a factorial of any number a factorial is a sum of all the numbers that come before a number

def factorial(value):
    if value == 1:
        return 1
    else:
        return value + factorial(value-1)
print(factorial(300))