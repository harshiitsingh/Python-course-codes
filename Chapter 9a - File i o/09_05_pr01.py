f = open('poem.txt')
t = f.read()

if 'twinkle' in t:
    print("Twinkle is present in the poem")
else:
    print("Twinkle is not present in the poem")
f.close()