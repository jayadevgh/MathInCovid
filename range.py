print("Welcome to the range game!")
import random
a=random.randrange(1,20)
b=random.randrange(1,20)
c=random.randrange(1,20)
print("The numbers are "+str(a)+", "+str(b)+", "+str(c))
print("Find the least number")
d=[a,b,c]
leastnum=a
#leastnum
for i in d:
    if i<leastnum:
        leastnum=i
y=int(input("Enter: "))
if y==leastnum:
    print("Correct!")
elif y!=leastnum:
    print("Incorrect")

greatestnum=b
if b<a:
    greatestnum=a
else:
    greatestnum=b
if c>greatestnum:
    greatestnum=c
rangeofdataset=greatestnum-leastnum
z=int(input("Enter range: "))
if z==rangeofdataset:
    print("Correct!")
elif z!=rangeofdataset:
    print("Incorrect")
