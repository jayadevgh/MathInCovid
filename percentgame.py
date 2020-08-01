print("Precent Game")
import random
x=random.randrange(1,100)
print("The number is "+str(x))
y=random.randint(1,100)
print("Find "+str(y)+"% of "+str(x))
def percent(x,y):
    return x*(y/100)
z=float(input("Enter answer: "))
if z==percent(x,y):
    print("Correct!")
if z!=percent(x,y):
    print("Incorrect")