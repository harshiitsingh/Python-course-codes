# Here's a dictionary that stores elements and their atomic numbers.

elements = {"hydrogen": 1, "helium": 2, "beryllium":4, "carbon": 7}
print(elements)

print(elements["helium"])  # print the value mapped to "helium"

elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print(elements)

#delete a entry
del elements["beryllium"]
print(elements)

# update a value
elements["carbon"]=6
print(elements)

print("carbon" in elements)  #to check whether the element is present or nor
print(elements.get("dilithium"))