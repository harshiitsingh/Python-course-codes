# Write a python program to rename a file to "renamed_by_python.txt"

import os

oldname = "ques 11.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, 'w') as f:
    f.write(content)

# till now we have only copied the file content in new file
# now by any how we can delete the oldfile then rename process can be executed successfully

# google--> how to delete a file using os module in python

# import os
os.remove(oldname)