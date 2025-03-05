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