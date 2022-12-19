# A dictionary is used to store data in key value pairs

myDict = {
    'Name': 'John',
    'USN': 23,
    'Course': 'ECE',
    'Batch': 2022 
}

# Accessing individual values
# print(myDict['Course'])

# Better way
print(myDict.get('Name'))
# print(myDict['Marks']) This throws an error because marks doesnt exist
print(myDict.get('Marks')) # Whereas this will give 'none'
print(myDict)

# Adding key
myDict['Phone'] = '343-434'
print(myDict)

# Updating dictionary
# myDict['Name'] = 'Ray'
# print(myDict)

# Better way
myDict.update({'Name': 'Jesse','USN': 35,'Batch': 2020})
print(myDict)

# Deleting a value
del myDict['Phone']
print(myDict)

# Pop an element and store it in another variable
usn = myDict.pop('USN')
print(usn)

# More functions
print(myDict.keys()) # Prints only key
print(myDict.values()) # Prints only values
print(myDict.items()) # Prints pairs of key and values