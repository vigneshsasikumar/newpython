# verify the type of an object
# x y z has some  values contains int, float and complex, while print this comment it will
# show what is the type present in it
# int - int or integer is a whole number, positive or negative  without decimals of unlimited strength
# float - float or floating point is number, positive or negative containing one or two decimals
# float can also be scientific numbers with an "e" to indicate the power of 10
# complex - complex number are written with a imaginary part "j" including negative

#example1

x = 2
y = 4.7
z = 7j

print(type(x))
print(type(y))
print(type(z))

#output
#int
#float
#complex


#example2 create integers
# int - int or integer is a whole number, positive or negative  without decimals of unlimited strength

a = 7
b = 5442535244344
c = -676476

print(type(a))
print(type(b))
print(type(c))

#output
#int
#int
#int


#example3 create floating points
# float - float or floating point is number, positive or negative containing one or two decimals
# float can also be scientific numbers with an "e" to indicate the power of 10

d = 4.56
e = 45.6
f = -67.04
g = 24e5
h = 32E6


print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

#output
#float
#float
#float
#float
#float



#example4 create complex numbers
# complex - complex number are written with a imaginary part "j" including negative

i = 2+4j
j = 3j
k = -9j

print(type(i))
print(type(j))
print(type(k))


#output
#complex
#complex
#complex


i = 4j
j = 3j
k = 2j

print(type(i))
print(type(j))
print(type(k))
