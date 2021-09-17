words = ["donkey","Donkey", "kaddu", "mote"]

with open("ques 5 sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("ques 5 sample.txt", 'w') as f:
        f.write(content)
'''
My name is mote Harshit Singh.
I lives in kaddu varanasi. Donkey
more lines please donkey
donkey
'''