#while loop -- in while loop we can execute as long as the statement is true

# print i as long as i is less than 9:
# while i<9 --> it will enter a value till it reaches  before 9, becuse i should less than 9

i = 1
while i < 9:
  print(i)
  i += 1
else:
  print("i is no longer less than 9")
  
  #output
  #1
  #2
  #3
  #4
  #5
  #6
  #7
  #8
  # i is no longer than 9
  
# break statement
# using this break statement , we can stop the loop, even while condition is true
# i == 4, the iteration will end at 4 and stop the loop

i = 1
while i < 9:
  print(i)
  if (i == 4):
    break
  i += 1
  
#output
#1
#2
#3
#4
  
  
#continue statement
# In continue statement , we can stop the current iteration and continue with the next iteration
# i == 4 , 4 will miss in the output becaue we use the continue statement, 


i = 0
while i < 7:
  i += 1
  if i == 4:
    continue
  print(i)
  
  
  #output
  #1
  #2
  #3
  #5
  #6
  #7
  
  
# write a program to print a even number
    
i = 0
while i <= 11:
  if i % 2 == 0:
    print(i)
  i+=1
  

# Write a Python Program to Print Even Numbers from 1 to N Using a while-loop

num = int(input("Enter a Number: "))
i = 0
while i <= num:
    if i % 2 == 0:
      print(i)
    i+=1
  
#Write a Python Program to Print Even Numbers in a given range Using a while-loop

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

while i<=num:
  if i%2 == 0:
    print(i)
  i+=1
  
  i=0
  while i <= 21:
    if i%2 == 0:
      print(i)
    i+=1
  
  

i=0
while i<=22:
  if i%2 == 0:
    print(i)
  i+=1
  
#simple quiz game

print("welome to my kungfu game! ")

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
  quit()
  
print("okay! lets play ")
score = 0

answer = input("what cpu stands for? ")
if answer.lower() == "central processing unit":
  print("correct")
  score += 1
else:
  print("incorrect")
  
answer = input("what ram stands for? ")
if answer.lower() == "random access memory":
  print("correct")
  score += 1
else:
  print("incorrect")
  
answer = input("what gpu stands for? ")
if answer.lower() == "graphics processing unit":
  print("correct")
  score += 1
else:
  print("incorrect")
  
answer = input("what psu stands for? ")
if answer.lower() == "power supply":
  print("correct")
  score += 1
else:
  print("incorrect")
  
print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 4) * 100) + "%")