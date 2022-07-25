def greet(name):
    print(f"Good Morning, {name}")

# n = input("Enter a name\n")
# greet(n)

# print(__name__)
if __name__ == "__main__":
    n = input("Enter a name\n")
    greet(n)

'''
__name evaluates to the name of the module in Python from where the program is ran.

If the module is being run directly from the command line, the __name__ is set 
to string "__main__".
Thus this behavious is used to check whether the module is run directly or
imported to another file.'''