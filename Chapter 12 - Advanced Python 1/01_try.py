# Exception handling in python

while(True):
    print("Press q to quit.")
    a = input("Enter a number: ")
    if a == 'q':
        break
    # a = int(a)
    # if a>6:
    #     print("You entered a number greater than 6.")

    try:
        print("Trying...")
        a = int(a)
        if a>6:
            print("You entered a number greater than 6.")
    except Exception as e:
        # print(e)
        print(f"Your input resulted in an error {e}")
    # Generally, if we make any error or input an error then the program ends there.
    # but using try and except, it will not kill the program rather kill the iteration and continue.

print("Thanks for playing this game")