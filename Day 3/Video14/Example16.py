#Nested if-else--------------


num=int(input("Enter no"))
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
        print("Number between 1-10")
    elif(num>10 & num<=20):
        print("Number between 10-20")
    else:
        print("Number gretter than 20")
else: 
    print("Number is 0")
    
    
    # from hare i push code in github