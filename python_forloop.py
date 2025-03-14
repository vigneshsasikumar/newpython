#for loop - for loop is iterating over a sequence either list, tuple, dictionary, set or string


kungfu = ["punch", "block", "kicks"]
for x in kungfu:
  print(x)

#output
#punch
#blocks
#kicks

#Loop through a string - it will contain a sequence of characters


for x in "kungfu":
  print(x)

#output
#k
#u
#n
#g
#f
#u


#break statement
# using this break statement , we can stop the loop, even while condition is true
# i == 4, the iteration will end at 4 and stop the loop

kungfu = ["punch", "block", "kicks"]
for x in kungfu:
  print(x)
  if x == "block":
    break

#output
#punch
#block
  

#continue statement -  In continue statement , we can stop the current iteration and continue with the next iteration
# x == block , block will miss in the output becaue we use the continue statement, 


kungfu = ["punch", "block", "kicks"]
for x in kungfu:
  if x == "block":
    continue
  print(x)
  
  #output
  #punch
  #kicks
  
  #range - it returns a sequence of numbers starting 0 by default and 
         # increment by 1 and ends at a specified number
 #range() - denotes by this command
 
for x in range(4):
  print(x)
  
#output
#0
#1
#2
#3


# else in for loop - The else keyword in a for loop specifies a block of code 
                     # to be executed when the loop is finished
#print all numbers from 0 to 5 and print message when the loop is ended

for x in range(4):
    print(x)
else:
    print("message for loop")
    
#output
#0
#1
#2
#3
#message for loop

#nested loop - A nested loop is a loop inside a loop
# The inner loop will be executed one time for each iteration of the outer loop

kungfu = ["punch", "block", "kicks"]
silambam = ["rotation", "attack", "show"]
for x in kungfu:
    for y in silambam:
        print(x,y)

#output
#punch rotation
#punch attack
#punch show
#block rotation
#block attack
#block show
#kicks rotation
#kicks attack
#kicks show

# Write a Python Program to Print Even Numbers from 1 to 20 Using a for-loop

for i in range(0,20):
  if i % 2 == 0: 
   print(i)

#Write a Python Program to Print Even Numbers in a given range Using a for-loop

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

for i in range(num1, num2+1):
  if i%2 ==0:
    print(i)
    

# Write a Python Program to Print Even Numbers from 1 to N Using a for-loop

num = int(input("Enter a Number: "))
for i in range(0,num+1):
  if i % 2 == 0:
    print(i)
    
    
# print the list of even numbers

for i in range(0,20):
   if i%2 == 0:
     print(i)