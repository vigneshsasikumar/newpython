#quiz

print("welcome to quiz game")

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
  quit()
  
print("okay! lets play ")
score = 0

answer = input("what sv stands for ")
if answer.lower() == "sv":
  print("correct")
  score += 1
else:
  print("incorrect")
  
answer = input("what mv stands for ")
if answer.lower() == "mv":
  print("correct")
  score += 1
else:
  print("incorrect")
  
print("you got " + str(score) + " questions correct!")
print("you got " + str((score/2) * 100) + "%")


#quiz game

print("welcome to play my fun game! ")

addition = input("Do you want to start the game? ")
if addition.lower() != "yes":
  quit()

print("okay! Lets start ")
score = 0

addition = input("1+1= ")
if addition.lower() == "2":
  print("correct answer")
  score += 1
else:
  print("incorrect answer")
  
subtraction = input("3-2= ")
if subtraction.lower() == "1":
  print("correct answer")
  score += 1
else:
  print("incorrect answer")

print("you got " + str(score) + " question correct")
print("you got " + str((score/2) * 100 ) + "%")