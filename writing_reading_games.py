# This code is for the writing lesson part of the website
# Between each writing game there should be a next button that will take you to the next game and a picture of an
# example and including with a link that should send you to a video which explains what the lesson is about and to do it
score = 0
print("Type in what is written to practice your writing skills.")
print("You gain points every time you type the sentence correctly. The total is 15 points and each problem is 5 points.")
input1 = str(input("It is so sunny outside, today. "))
if input1 == "It is so sunny outside, today.":
    print("Good Job! Good typing!")
    score += 5
else:
    print("Nice Try. Copy the sentence exactly.")
input2 = str(input("The village groceries store has the root vegetable called carrots."))
if input2 == "The village groceries store has the root vegetable called carrots.":
    print("Good Job! Wonderful Typing!")
    score += 5
else:
    print("Nice Try. Copy the sentence exactly.")
input3 = str(input("The clouds are moving really fast today because of the strong winds. "))
if input3 == "The clouds are moving really fast today because of the strong winds.":
    print('Good Job. Incredible typing!!')
    score += 5
else:
    print("Nice Try. Copy the sentence exactly.")
print('Your score is ' + str(score))
#-----------------------------------------------------------------------------
# this game will help learn to create grammatical sentences

#This is the code that needs to be added into the Pycharm folder of Hackathon
print("Change the sentences below so that the sentence is said correctly")
print("You will get 5 points for each question you get right and there are 4 questions")
print("This is the format how your answer should look like ---")
print("--> {The thing that needs to be changed}; the sentence with the change")

score = 0
input_one = str(input("That ball over their belongs to that kid over there.") )
if input_one == "{there}; That ball over there belongs to that kid over there":
    print("Great job. You earned 5 points")
    score += 5
else:
    print("Nice Try, better luck next time.")

input_two = str(input("We saw two mouses running through the field. "))
if input_two == "{mice}; We saw two mice running through the field":
        print("Good Job. You earned five points!!")
        score += 5
else:
        print("Nice Try, better luck next time.")

input_three = str(input("I am more big than you"))
if input_three == "{bigger}; I am more bigger than you":
    print("Good Job, You earned five points!!")
    score += 5
else:
    print("Nice Try, better luck next time.")


input_four = str(input(" I is very thirsty"))
if input_four == "{am}; I am very thirsty":
    print("Amazing Job, You earned five points!")
    score += 5
else:
    print("Nice Try, good effort")

print("Your score is " + str(score) + "out of 20")

#-----------------------------------------------------------------------------
# This game is a spelling test game which helps understand and learn spelling
# add a recording that says the words so that they can spell it in the website
print("Listen to the word in the recording and enter the spelling of the word in the space below")
score = 0
input_spell1 = str(input(""))
if input_spell1 == "apple" or input_spell1 == "Apple":
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the correct spelling is \'apple\'.")

input_spell2 = str(input(""))
if input_spell2 == "hopping" or input_spell2 == "Hopping":
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the correct spelling is \'hopping\'.")

input_spell3 = str(input(""))
if input_spell3 == "brought" or input_spell3 == "Brought":
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the correct spelling is \'brought\'")

input_spell4 = str(input(""))
if input_spell4 == "Borrowed" or input_spell4 == 'borrow':
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the correct spelling \'borrow\'")

input_spell5 = str(input(""))
if input_spell5 == "cowboy" or input_spell5 == "Cowboy":
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the scorrect spelling is \'cowboy\'")

input_spell6 = str(input(""))
if input_spell6 == 'welcome' or input_spell6 == 'Welcome':
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the correct spelling is \'welcome\'.")

input_spell7 = str(input(""))
if input_spell7 == "garden" or input_spell7 == "Garden":
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the correct spelling \'garden\'.")

input_spell8 = str(input(""))
if input_spell8 == 'subterranean' or input_spell8 == 'Subterranean':
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the correct spelling \'subterranean\'.")

input_spell9 = str(input(""))
if input_spell9 == "politician" or input_spell9 == "Politician":
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the correct spelling \'politician\'/")

input_spell10 = str(input(""))
if input_spell10 == "exaggerate" or input_spell10 == "Exaggerate":
    print("Correct Answer!!!")
    score += 1
else:
    print("Incorrect answer, the correct spelling \'exaggerate\'.")

print("Your score is " + str(score))
# That would be the last game or thing you have to do for the writing and reading part of the learning
# at home educational website...
