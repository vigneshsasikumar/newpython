# if statement --> An if statement is written using if keyword

# a simple if statement
# if statement is true , it will print the statement

forms = 20
attack = 15

if forms > attack:
  print("forms are technically stronger than attack")

#output
#forms are technically stronger than attack

# elif statement
# elif --> if previous statements are not true, then try this condition
forms = 20
attack = 15

if forms > attack:
  print("forms are technically stronger than attack")
elif forms == attack:
  print("forms are eqaual to attack")
  
  
#output
#forms are technically stronger than attack

#else statement
# else - if the previous statement is not passed, else keyword will satisfy the condition

forms = 20
attack = 15

if attack > forms:
  print("attack are technically stronger than forms")
elif forms == attack:
  print("forms are equal to attack")
else:
  print("forms are technically stronger than attack")

  
#output
#forms are technically stronger than attack
  
  
#shorthand if statement
# if we have only one statement to execute, then we can put in the same line with if statement
  
forms = 20
attack = 15

if forms > attack: print("forms are technically stronger than attack")
  
#output
#forms are technically stronger than attack


#shorthand if...else
# # if we have only one statement to execute, one for if and one for else 
# then we can put in the same line with if..else statement

forms = 10
attack = 15

print("forms are technically stronger than attack") if forms > attack else print("kungfu is best")
  
  
  #output
  #kungfu is best
  
# The And Keyword
#The and keyword is a logical operator and it is used to combine conditional statements
  
punches = 5
blocks = 3
kicks = 10

if punches > blocks and kicks > punches:
  print("punches and kicks are powerful to practice")
  
  
  #output
  #punches and kicks are powerful to practice
  
  
# The or Keyword
#The or keyword is a logical operator and it is used to pass the statement if one condition is true
  
punches = 5
blocks = 3
kicks = 1

if punches > blocks or kicks > punches:
  print("punches and kicks are powerful to practice")
  
  
  #output
  #punches and kicks are powerful to practice

# factorial of a number

n = int(input())

res = 1
if n<0:
  res = 0
elif n==0 or n==1:
  res = 1
else:
  while n>1:
    res = res * n
    n -= 1
print("factorial is ",res)

#Compare Two Numbers using the else-if statement and output smaller and larger numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1>num2:
  print(f"Larger number: {num1}")
  print(f"Smaller number: {num2}")
  
elif num1<num2:
  print(f"Larger number: {num2}")
  print(f"Smaller number: {num1}")

else:
  print("Both numbers are equal")
  
  
# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Take input from the user
year = int(input("Enter a year: "))

# Check and display the result
if is_leap_year(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is NOT a Leap Year.")
    
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