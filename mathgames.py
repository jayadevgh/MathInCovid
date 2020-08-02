print("Hello World")
import random
import math
import operator
def get_random_numbers():
   # get_random_numbersglobal player1score
   #return ('Welcome to the pythagorean thereom game!')
   #return ("Please round down your answer")
   a = random.randrange(1,20)
   b=random.randrange(1,20)
   return(a,b)
def get_random_operator():
   operation=random.choice(['+', '-', '*','/'])
   return operation

def operation_game(operation, num_1, num_2):
   operators = {
      '+': operator.add,
      '-': operator.sub,
      '*': operator.mul,
      '/': operator.truediv,
   }
   answer=operators.get(operation)(num_1,num_2)

def pythagorean_game(a, b, result):
   answer = math.floor((a ** 2 + b ** 2) ** (1 / 2))
   player1score = 0
   if (answer==result):
      player1score=player1score+1
      return("CORRECT! Take some cookie points!")
   elif (answer!=result):
      return("Incorrect")

