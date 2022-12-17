# Multiple variables
x, y, z = "One","Two","Three"
print(x,y,z)

# Assigning same value
x = y = z ="Four"
print(x)

# Unpacking a list
alphabets = ["a","b","c"]
x, y, z = alphabets
print(x , y , z)

# Global variable
# Every variable in python is a global variable if it's not in a function

msg = "of code" #Global variable
def func():{
    print("This is a line "+ msg)
}
func()

def func2():
    msg = "apple" #Local variable
    print("This is " +msg)
func2()
func()

# Global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic" # x becomes global

myfunc()

print("Python is " + x)