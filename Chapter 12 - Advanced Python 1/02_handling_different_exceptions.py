try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
except Exception as e:
    # print("Exception1 occured")
    print("Please enter a valid value")
    # print(e) # here python is printing e not an error producing...also we can print e or cannot depends on user.
    # pass

except ZeroDivisionError as e:
    # print("Exception2 occured")
    print("Make sure you are not dividing by 0")
    # print(e)

print("Thanks for using this code!")