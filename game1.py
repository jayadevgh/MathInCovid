print("Hello World")
import random
import math
def round1():
   global player1score
   print ('Welcome to the pythagorean thereom game!')
   print("Please round down your answer")
   a=random.randrange(1,20)
   b=random.randrange(1,20)
   print(a)
   print(b)
   x=math.floor((a ** 2 + b ** 2) ** (1 / 2))
   player1score=0
   player2score=0
   y=float(input("Enter: "))
   if (x==y):
       player1score=player1score+1
       print("CORRECT! Your score is "+ str(player1score))
   elif (x!=y):
       print("Incorrect")
def round2():
   global player1score
   print("Welcome to round 2")
   print("Please round down your answer")
   f=random.randrange(1,20)
   g=random.randrange(1,20)
   print(f)
   print(g)
   w=math.floor((f ** 2 + g ** 2) ** (1 / 2))
   z=float(input("Enter: "))
   if (w==z):
       player1score=player1score+1
       print("CORRECT! Your score is "+ str(player1score))
   elif (w!=z):
       print("Incorrect")
def round3():
   global player1score
   print("Welcome to round 3")
   print("Please round down your answer")
   h=random.randrange(1,20)
   i=random.randrange(0,20)
   print(h)
   print(i)
   j=math.floor((h ** 2 + i ** 2) ** (1 / 2))
   k=float(input("Enter: "))
   if (j==k):
       player1score=player1score+1
       print("CORRECT! Your score is "+ str(player1score))
   elif (j!=k):
       print("Incorrect")
round1()
round2()
round3()
global player1score
print("Congratulations! You got "+str(player1score)+"/3")
