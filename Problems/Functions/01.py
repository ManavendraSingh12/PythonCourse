# Write a Python function to find the Max of three numbers.

a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

def myFunc(a,b,c):
    return max(a,b,c)

maxNum = myFunc(a,b,c)
print("Max number is: " +str(maxNum))