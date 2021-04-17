for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for")
# Therefore, else will only execute when for loop will successfully and completely execute.
# Here, for loop breaks at 5,hence else will not run.