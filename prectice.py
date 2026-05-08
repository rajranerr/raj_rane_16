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
