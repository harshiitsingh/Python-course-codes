# Dictionary is a collection of key-value pairs.
myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 5],
    "anotherDict": {'harry': 'Player'} # nested dictionary
}

print(myDict['Fast'])
print(myDict['Harry'])
print(myDict['Marks'])
print(myDict['anotherDict'])
print(myDict['anotherDict']['harry'])
# mutable
myDict['Marks'] = [45, 78]
print(myDict['Marks'])