pr1 = input("My balloon went all the way into outer _____.:")
score=0
if pr1 == 'space':
    print("Correct, you got the right answer!")
    score+=1
else:
    print("incorrect, answer is space")

pr2 = input("Why does my ice cream always ____ underneath the sun?:")
if pr2 == 'melt':
    print("Correct, you got the right answer!")
    score += 1
else:
    print("incorrect, answer is melt")

pr3 = input("Basketball is a really fun _____ even though it is very simple.: ")
if pr3 == 'sport':
    print("Correct, you got the right answer!")
    score += 1
else:
    print("incorrect, answer is sport")

pr4 = input("We all had to _____ and say cheese for the picture.:")
if pr4 == 'smile':
    print("Correct, you got the right answer!")
    score += 1
else:
    print("incorrect, answer is smile")

pr5 = input("I tried to ____ over the large puddle.:")
if pr5 == 'jump':
    print("Correct, you got the right answer!")
    score += 1
else:
    print("incorrect, answer is jump")
print("You score is "+str(score)+"/5")
