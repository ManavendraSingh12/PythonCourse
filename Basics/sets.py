# Sets are used to stote multiple elements in a single variable in an unordered list 
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

mySet = {'apple','mangoes','kiwi'}
print(mySet)

# print('apple' in mySet) Checks T or F
myDish = {'apple','banana','cucumber','kiwi'}
print(mySet.intersection(myDish)) # Prints commmon elements
print(mySet.difference(myDish)) # Prints uncommon elements
print(mySet.union(myDish)) # Combines sets

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This creates an empty dict not an empty set
empty_set = set() # To create an empty set