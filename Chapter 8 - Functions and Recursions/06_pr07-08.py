# Q.7 Write a python function to remove a given word from a string (list) and strip it at the same time.

# meaning of strip
a = "    Harshit    singh  .    "
print(a)
print(a.strip())

def remove_and_split(string,word):
    newStr = string.replace(word, "")
    # return newStr.split()
    return newStr.strip()

this = "  Harry is a coder     "
n = remove_and_split(this, "Harry")
print(n)

# Q.8 Write a python function to print multiplication table of a given number.