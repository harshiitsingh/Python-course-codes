a = 34
b = "Harry" # or b = 'Harry' or b = '''Harry'''
print(a,b)
print(type(a),type(b))

# why three types of quotes made or used?
# b = 'Harry's' here python interpreter become confuse
b = "Harry's" # --> use this if you have single quotes in ur strings
print(b)

b = '"Harry"'
c = 'Harry"s'
d = '''Harry"s and Harry's''' 
e = '''Harry"s and

 Harry's''' 
f = '''Harry"s and
             Harry's''' 
print(b,c,d,e,f)