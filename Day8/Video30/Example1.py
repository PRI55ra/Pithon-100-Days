def factorial(n):
    if (n == 0 or n == 1):
        return 1  
    else:
        return n * factorial(n - 1)

y = int(input("Enter a number: "))
print(factorial(y))
