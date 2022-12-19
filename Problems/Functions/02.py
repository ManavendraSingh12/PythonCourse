# Write a Python function to sum all the numbers in a list.

n = int(input("Enter number of elements : "))
  
# Below line read inputs from user using map() function 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

def myFunc(a):
    print(sum(a))
  
print("\nList is - ", a)

 
myFunc(a)


# Below line read inputs from user using map() function
# a = list() 
# def myFunc(a):
#     Sum = sum(a)
# a = (map(myFunc,input("\nEnter the numbers : ").strip().split()))
  
# print("\nList is - ", a)
# b = myFunc(a)
# print(b)

# list = [1,2,3]
# print(sum(list))

# a = list(int(input("\nEnter the numbers : ").strip().split()))
# n = input()
# a = (map(int,input("\nEnter the numbers : ").strip().split()))[:n]
# # b = sum(a)
# print(a)

# def myFunc(a):
#     print(sum(a)) 
# myFunc(a)
# print(myFunc(a))


