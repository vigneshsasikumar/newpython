#strings - strings in python are surrounded by single quotation marks or either double quotation marks
#example -> print('Hello') and print("Hello") both are same 

# example1 -> get the character at the position 1 of a string  
# It starts with 0123456789

a = "Welcome, Namaste!"
print(a[1])


#output
#e

#example2 -> substring. get the characters from position2 to position5
# It starts with 0123456789( character position starts from 2 to 5)

b= "Chennai, City"
print(b[2:5])


#output
#enn

# example3: -> remove the whitespace from the begining or end of the of a string
# use strip() command to clear the space from starting or end of the string

c = " New, Home! "
print(c.strip())

#output
#New, Home!

#example4 -> return the length of the string
# use len(value) command to know the length of the string


d = "Kungfu, Master"
print(len(d))

#output
#14

#example 5 -> convert a string to lowercase
#use variable.lower() command to change the uppercase to lowercase


e = "Change, Lowercase!"
print(e.lower())

#output
#change, lowercase!


#example6 -> convert a string to uppercase
#use variable.upper() command to change the uppercase to lowercase


f = "Change, Uppercase!"
print(f.upper())


#output
#CHANGE, UPPERCASE!


#example7 -> Replace a string with another string
# use variable.replace() command to replace string with another string


g = "Wow, Nice!"
print(g.replace("W", "N"))

#output
#Now, Nice!

#example8 -> split a string into substring
# use variable.split(",") command to split a string into substring

h = "TajMahal, NewDelhi"
i = h.split(",")
print(i)


#output
#'TajMahal', 'NewDelhi'