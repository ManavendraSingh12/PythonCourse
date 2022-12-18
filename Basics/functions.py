# Functions are defined using def keyword
def myFunc():
    print("Hello world")

myFunc()

# Function with arguments
name = input("Enter your name:")
def myFunc(name):
    print("Hello "+name)
myFunc(name)

# Parameter: A variable listed inside function definition
# Arguments: Information sent to function 

def info(name,email):
    print("Name:"+name+"\n"+"Email:"+email)
name = input("Enter your name")
email = input("Enter your email")
info(name,email)

# Arbitary Functions
# - Used if you don't know how many arguments will be passed
# - function will recieve a tuple of arguements
def arbFunc(*fruits):
    print(fruits[1])
arbFunc("Apple","Orange","Mango")

# Default parameter value 
# If we call a function without parameter it uses the default value
def myCountry(country = "India"):
    print("I am from "+country)
myCountry("Sweden")
myCountry("Japan")
myCountry("Mexico")
myCountry() # Will print default value


# Passing list as an argument
def cart(food):
    print(food[1])
food = ["Apple","Orange","Mango"]
cart(food)

# Return values
def mul(x):
    return x * 2
print(mul(2))
print(mul(3))
print(mul(4))

# Common built in functions

# abs() : returns absolute value 
x = abs(-34.32)
print(x)


# pow() : power of a number
x = pow(2, 3) # = 2 * 2 * 2
print(x)

# min() : returns minimum number
x = min(43535,3234)
print(x)

# max() : returns maximum number
x = max(43535,3234)
print(x)
