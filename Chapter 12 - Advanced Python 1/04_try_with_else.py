
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else: # it will run only when try will not goes in except
    print("We were successful")
