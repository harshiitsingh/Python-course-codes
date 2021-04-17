# Dictionary Data type
# A dictionary is like a list but instead of looking up an index to access values , we will use a uniquely key 
# which can be a number string or tuple
# dictionary value can be anything but key must be immutable type
# { key:dictionary}
d = {"suman":1,"shalini":2,'nisha':3,'sona':4}
print(d)
# add entry
d["nitish"]=5
print(d)
#delete entry
del d["sona"]
print(d)
# update valued
d["shalini"]=22
print(d)
#remove all entries
d.clear()
print(d)
# delete dictionary
del d
print(d)