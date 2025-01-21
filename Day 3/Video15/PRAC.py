import time
a= time.strftime('%H:%M:%S')
print(a)
b= int(time.strftime('%H'))
print(b)
if(6>b):
    print("Go to sleep \n you are too late")
elif(6<=b<=10):
    print("Good morning Baby")
elif(10<b<12):
    print("you are too late \n Good Morning")
elif(12<=b<18):
    print("Good Afternoon")
elif(18<=b<21):
    print("Good Eveming")
else:
    print("Good Night")
    

