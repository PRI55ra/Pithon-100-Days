def calculate(a,b):
    mean=(a+b)/2
    print(mean)
    
def graterthan(a,b):
    if(a>b):
        print("First number is bigger")
    else:
        print("Secound no is gratter")

a=int(input("Enter the 1st value"))
b=int(input("Enter the 2nd value"))

calculate(a,b)
graterthan(a,b)

c=int(input("Enter the 1st value"))
d=int(input("Enter the 2nd value"))

calculate(c,d)
graterthan(c,d)