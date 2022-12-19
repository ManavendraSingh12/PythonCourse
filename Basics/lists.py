# Lists are just like arrays
# A list is a collection of things enclosed in [ ] brackets

# Declaration
myList = [1,2,3]
print(myList)

myList = ["Fruits", "Vegetables", "Juices"]
print(myList)

myList = ["Fruits", 1, "Water", 23434, "Vegetables"]
print(myList)

# Declaration using constructor
myList = list((1,2,3))
print(myList)


# Accessing a List
# One dimentional List 
List = ["Fruits", 1, "Water", 23434, "Vegetables"]
print(List[2])

# Multi dimentional List
List = [ ['Dog', 'Cat'], ['Animals']]
print(List[0][1])
print(List[1][0])

# Negative Indexing
newList = [1,3,"apple",534,"Human",343,"Number",34]
print(newList[-1]) # -1 refers to the last element
print(newList[-2]) # -2 refers to the second last element

numbers = [54,234,545,3234,23,422]
numbers.sort(); # Small to big
numbers.reverse(); # Reverse
numbers.append(10) # Adds to last
numbers.remove(234) # Removes element
numbers.insert(2,333) # First argument index ; Second argument element
numbers.pop() # Removes last element

print(numbers) 





