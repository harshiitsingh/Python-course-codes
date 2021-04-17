myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1, 2, 5],
    "anotherDict": {'harry': 'Player'}, # nested dictionary
    1: 2
}

print(myDict.keys()) # this will print the keys of the dictionary in the form of list
print(type(myDict.keys()))
print(list(myDict.keys())) # type casting into list
print(myDict.values())

print(myDict.items()) # Prints the (keys,values) for all the contents of the dictionart

# updating dictionary
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Shubham": "Friend",
    "harry": "A dancer"  #update the value from old or previous key
}
myDict.update(updateDict)  # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("harry")) # Prints value associated with the key "harry"
print(myDict["harry"]) # Prints value associated with the key "harry"
# But the difference b/w .get and [] syntax in Dictionaries : ?
print(myDict.get("harry2")) # Returns None as harry2 is not present in the dictionary
print(myDict["harry2"]) # throws error as harry2 is not present in the dictionary

# for more methods google, python dictionary method