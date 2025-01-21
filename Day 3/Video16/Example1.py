x=int(input("Enter the value:"))

match x:     #this is error because this match statement needed 3.10 version of python
    case 0:
        print("x is Zero")
    case 4:
        print("x is 4")
    case _:
        print("x is x")