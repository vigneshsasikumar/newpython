#for loop - for loop is iterating over a sequence either list, tuple, dictionary, set or string


kungfu = ["punch", "block", "kicks"]
for x in kungfu:
  print(x)



#break statement

kungfu = ["punch", "block", "kicks"]
for x in kungfu:
  print(x)
  if x == "block":
    break
  

#continue statement

kungfu = ["punch", "block", "kicks"]
for x in kungfu:
  if x == "block":
    continue
  print(x)