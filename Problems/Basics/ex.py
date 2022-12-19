# To swap 2 variables
a = 10
b = 20
print(a, b)
a , b = b, a
print("a: "+str(a) + "b: "+str(b))

# Product of 3 variables
x,y,z = 2,4,8
# print (x*y*z)
print("Product is ",x*y*z)

# Square of 2 numbers
num = int(input("Enter number: "))
print("Square of ",num, "is",(num*num))

# Print
name = str(input("Enter your name: "))
rollno = int(input("Enter your rollno: "))
foi = str(input("Enter your field of interest: "))
print("Hello, my name is ",name," and my roll number is ",rollno," . My field of intrest is ", foi)