def fevo(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        f= fevo(n - 1) + fevo(n - 2)  # Recursive call
        return f
m = int(input("Enter a Number: "))
print(fevo(m))



