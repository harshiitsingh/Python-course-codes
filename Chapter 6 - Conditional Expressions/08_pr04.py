# Q.4 Write a program to find whether a given username contains less than 10 characters or not.
# use len fxn 

userName = input("Enter the username: ")
if len(userName)<10:
    print("The user name has less than 10 characters.")
else:
    print("The username has more than or equal to 10 characters.\n")