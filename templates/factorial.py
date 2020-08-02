import random
import operator
import math

#function that calculates the factorial n
def fact(n):
   if n == 0: return 1;
   else: return n*fact(n-1)

def random_problem():
    num = random.randint(1,10)
    a = fact(num);
    print(f'What is Factorial of {num}:')
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
