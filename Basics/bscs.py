print("Hello world")

# VARIABLES
# Every variable in Python is an object.
# a = 4
# b = 5
a, b = 3, 5
print(a,b)

# Float
flt = float(10)
myfloat = 12.3
print(myfloat,flt)

# Strings
msg = "Hello world"
print(msg)
msg1 = "This is" + " a line of code"
print(msg1)

print(type(a))
print(type(myfloat))
print(type(msg))
# str + int is not supported in python
# print("Sum: " + (a+b))

# INPUTS
print("Enter length")
l = input()
print("Enter breadth")
b = input()
print ("The length is ",int(l)*int(b))