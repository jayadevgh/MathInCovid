import random
import operator
import math


#function that calculates are of a circle
#def area_of_circle():
#   a = r**2 * PI
#   return a
PI=3.14
def random_problem():
    r = random.randint(1,10)
    a = r**2 * PI
    print(f'What is Area of a circle with radius of {r}:')
    return a

def ask_question():
    answer =random_problem()
    guess=float(input())
    return guess ==answer

def game():
 print("How well do you know math?\n")
 score=0
 for i in range(10):
  if ask_question()==True:
   score +=1
   print("Correct!")
  else:
      print("Incorrect!")
 print(f'Your score is {score}')
game()


