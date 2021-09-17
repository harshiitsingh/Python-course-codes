try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally: # it will run irrespective of the whatever happen in/with except 
    print("We are done!")
    # executed regardless of error also if 'except' quit the program then also it will run

# print("We are done!")
print("Thanks")