'''
JOIN METHOD (string): creates a string from iterable objects (like list, tuple)
It will return a string using a "separator"
'''
l = ["Camera", "Laptop", "Phone", "iPad", "Hard Disk", "Nvidia Graphic Card"]
# l = ("Camera", "Laptop", "Phone", "iPad", "Hard Disk", "Nvidia Graphic Card")

# sentence = " and ".join(l)
# sentence = "~~".join(l)
# sentence = "==".join(l)
sentence = "\n".join(l)
print(sentence)
print(type(sentence))
