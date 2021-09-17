with open("ques 4 sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#") # what if we want to replace more than 1 word with same word

with open("ques 4 sample.txt", 'w') as f:
    f.write(content)
