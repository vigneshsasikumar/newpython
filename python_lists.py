#Lists - lists is used to store multiple items in single variable
# Lists is a collection which is ordered and changeable. Allow duplicate member
#Tuple - Tuple is a collection which is ordered and unchangeable. Allow duplicate values
#Sets - sets is  a collection  which is unordered , unchangeable unindexed. no duplicate values
#Dictionary - is a collection which is ordered, and changeable. no duplicate values

# create a list
# thislist = ["", "", ""] --> command used to create the list

thislist = ["Shaolin", "Master", "Vignesh"]
print(thislist)

#output
#['Shaolin', 'Master', 'Vignesh']

# Access list items
# to access the list items, use character position

thislist = ["Shaolin", "Master", "Vignesh"]
print(thislist[1])

#output
#Master

# Change the value of a List item
# to change the value , use character position

thislist = ["Shaolin", "Master", "Vignesh"]
thislist[1] = "Kungfu"
print(thislist)

#output
#['Shaolin', 'Kungfu', 'Vignesh']


# loop through a list
#using for loop in thislist , it will arrange one by one

thislist = ["Shaolin", "Master", "Vignesh"]
for x in thislist:
  print(x)
  
  
  #output
  #sholin
  #kungfu
  #vignesh


# check if a list item exists
# check the name present in thislist using --> if " " in this list:


thislist = ["Shaolin", "Master", "Vignesh"]
if "Vignesh" in thislist:
 print("yes,'Vignesh' is in the Shaolin Temple India" )


#output
#yes, 'Vignesh is in the Shaolin Temple India'