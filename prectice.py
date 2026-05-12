print("hello world")

# Basic Arithmetic:

a,b=4,6
print(f"addition: {a+b}")
print(f"division: {a/b}")

# Vaariable swepping:

x,y=7,4
x,y=y,x
print(x,y)

# If-Else Condition:

num=8
if num % 2 == 0:
    print("even")
else:
    print("odd")    

# Loops:

for i in range(4):
    print(i)    

# defining a function:

def greet(name):
    return f"Hello, {name}!"

print(greet("tilak"))

# Data structures:
  
# list opretions:

fruits=["apple","banana"]
fruits.append("mango") #add to end
print(fruits[1])  #accesses

#dictionary lookup:

student = {"name":"nupur","age":17}
print(student["name"])

#list comprehension:

squares = [x**2 for x in range(1,10)]
print(squares)


# A simple voting eligibility checker:

age_input = input("Enter your age: ")

age = int(age_input)

if age >= 18:
    print("you are eligible to vote.")
else:
    print("you are not eligible tio vote.")

# A simple calculator (user input):

N1 = input("Enter first number:")
N2 = input("Enter second number:")

sum_result = float(N1)*float(N2)

print(f"The multiplication of {N1} and {N2} is {sum_result}")

# number guessing game :

import random

secret_number = random.randint(1,10)
guess = None

print("I'm thinkink of a number between 1 and 10...")

while guess != secret_number:
    guess = int(input("take a guess:"))
    
    if guess < secret_number:
        print("too low! try again.")
    elif guess > secret_number:
        print("too high! try again.")
    else:
        print("congratulations! you got it.")


# square root function:

import math
 
x=math.sqrt(40)
print(x)

# pi function

import math

x=math.pi
print(x)

# area of triangle:

A=float(input("enter the base of the triangle:"))
B=float(input("enter the height of the triangle:"))
area = 0.5*A*B
print(f"The area  of the triagle is : {area:.2f}")


# area of circle:

import math

radius = float(input("enter the radiur of the circle:"))

area = math.pi*(radius**2)

print(f"the area of the circle with radius {radius} is:{area:2f}")

# Sequenced data:

#list:
      #example:

list1 = [0,5,4,[-4,6],["qpple","banana"]]
print(list1)

# tuple:
        # example:

tuple1 = (("parrot","sparow"),
          ("lion","tiger"))
print(tuple1)        

# mapped data :dict

dict1 ={"name":"kushu","age":18,"canVote":True }
print(dict1)   

# Arithmetic operator:

n=18
m=6

num1=n+m
print("addition of",n,"and",m,"is",num1)
num2=n-m
print("subtraction of",n,"and",m,"is",num2)
num3=n*m
print("multiplication of",n,"and",m,"is",num3)
num4=n/m
print("divition of",n,"and",m,"is",num4)
num5=n%m
print("modulus of",n,"and",m,"is",num5)
num6=n//m
print("floor divition of",n,"and",m,"is",num6)
num7=n**m
print("exponential of",n,"and",m,"is",num7)

# defining a function

def check_age(age):
    if age >=18:
        return "you are an adult."
    else:
        return "youare an minor."
    
# Calling the function 

user_age =20
result = check_age(user_age)
print(result)

# calculate square 

def square(num):
    return num*num

number =float(input("please enter any numeric value:"))

sqre = square(number)

print("the square  of a given number {0}={1}".format(number,sqre))

# passed or failed program

average =input('enter  average :')
if(int(average)>=50 ):
    print("passed")
else:
    print("failed")
    
 # simple interest 

p=float(input("enter principle(p):"))
t=float(input("enter time(t):"))
r=float(input("enter rate of interest(r):"))

si=(p*t*r)/100
print(si)

# swap two variables:

# input two  variables
a = input("enter the value of first variable (a):")
b = input("enter the value of sacond variable (b):")
# display the original values
print(f"original values: a = {a}, b = {b}")
# swap the value using a temporary variable
temp = a
a = b
b = temp
# display swapped values
print(f"swapped values:  a = {a}, b = {b}")

# generate a randome number:

import random
print(f"random number: {random.randint(1,200)}")

# convert kilometer to miles:
kilometers = float(input("Enter distance in kilometers:"))

# conversion_factor: 1 kilometers = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles} miles")

# Display calender

import calendar

year = int(input("enter year: "))
month = int(input("enter month: "))
cal = calendar.month(year,month)
print(cal)


# checking number is positive , nagative or zero

num = float(input("enter a number: "))
if num > 0:
    print("this is a positive number.")
elif num == 0:
    print("this is a zero.")
else:
    print("this is a negetive number.")

# check if number is odd or even

num = float(input("enter a number: "))
if num%2 == 0:
    print("this is a even number.")
else:
    print("this is a odd number.")

# upper and lower function:

text = "My home Town iS HAIdarPUr"
# for upper case:
print(text.upper())
# for lower case:
print(text.lower())

# split function:
name = "i am raj rane."
# for split
print(name.split())

# replace function: 

text = "I like bananas. But, Bananas is sweet."

# replece all occurences:
result = text.replace("bananas","apples")
print(result)

# replace only the first occurence:
result = text.replace("s","z",1)
print(result)

# remove a word:
result = text.replace("swwet","")
print(result)

