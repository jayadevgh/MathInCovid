print("Hello World")
y=int(input("How many values: "))
import random
sum=0
for b in range(y):
    b=random.randrange(0,10)
    print(b)
    sum=sum+b
average=sum/y
z=float(input("Enter the average: "))
if z==average:
    print("Correct!")
elif z!=average:
    print("Oops, Incorrect")