#Write a Python Program to Print Even Numbers from 1 to 100 Using a Function

def even_10():
  for i in range(0, 10+1):
    if i % 2 == 0:
      print(i)
    
even_10()

#Write a Python Program to Print Even Numbers from 1 to N Using a Function

def even_numbers(N):
 for i in range(0, N+1):
  if i%2 == 0:
    print(i)

num = int(input("Enter the number: "))
even_numbers(num)

#Write a Python Program to Print Even Numbers in a given range Using a Function

def Even_range(n1,n2):
    for i in range(n1, n2+1):
        if i%2 == 0:
            print(i)
            
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number :"))

Even_range(num1,num2)


# find the factorial of a number

def factorial(n):
    return 1 if (n<=1) else n*factorial(n-1)

n = int(input())
print(factorial(n))


