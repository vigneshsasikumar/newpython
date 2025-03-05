# Arithmethic operator - Arithmethic operators are used to perform mathematical operations

# Addition Operator - It is used to add the values
# (a + b) command is used to add values

a = 4
b = 4
print(a + b)


#output
#8

# Subtraction Operator - It is used to subtract the values
# (c - d) command is used to subtract values

c = 4
d = 2
print(c - d)


#output
#2


# Multiplication Operator - It is used to Multiply the values
# (e * f) command is used to Multiply values

e = 4
f = 2
print(e * f)


#output
#8

# Division Operator - It is used to Divide the values
# (g / h) command is used to Divide values

g = 4
h = 2
print(g / h)


#output
#2

# Modulus Operator - It will show the remainder 
# (i % j) command is used to show the remainder
# Exponentiation operator - It will calculate power of given values
# (i ** j) - ** denotes power of values
# Floor Division operator - It will show the quotient
# (i // j) - // denotes quotient


i = 11
j = 4
print(i % j)
print(i ** j)
print(i // j)

#output
#3
#14641
#2


# Assignment Operator - Assignment operator are used to assign values to a variables

#Add

x = 5
x += 4
print(x)

#output
#9

#sub

x = 4
x -= 2
print(x)

#output
#2

#Multiply

x = 2
x *= 5
print(x)

#output
#10

#Divide

x = 2
x /= 2
print(x)

#output
#1.0

#remainder

x = 6
x %= 3
print(x)

#output
#0

#Quotient

x = 8
x //= 4
print(x)

#output
#2


# Comparison Operator : It is used to compare two values

#Equal - Compare both values are equal and give the output
# both values are equal , it will show true
# both values are not equal, it will show false
# (a == b) command denotes equal 

a = 3
b = 2
c = 3
print(a == b)
print(a == c)
#output
#False
#True

#not equal
# (a != b) command denotes not equal 
# if a is not equal to b, it will enter true

a = 4
b = 7

print(a != b)

#output
# True

# Greater than
# Less than
# Greater than or equal to
# less than or equal to

a = 5
b = 4
c = 6
d = 7
print(a > b)
print(a < b)
print(c >= d)
print(c <= d)

#output
# True
# False
# False
# True


# Python logical operators - there are 3 operators AND , OR , NOT 
# AND operator - Only it will return True, when both values are true, If one value is false it will return false
# OR Operator - it will return True, one value is true itself, only it will return as false both values are false
# NOT operator  - it is used to reverse the result

# AND operator
x = 5
print(x > 6 and x < 7)

#output
#False


# OR operator
x = 8
print(x > 6 or x <9)

#output
#False

# NOT operator
x = 3
print(not(x > 4 and x < 8))

#output
#True