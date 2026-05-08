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