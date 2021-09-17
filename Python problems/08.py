# Write a program that accepts a sentence as input and calculates the number of letters, digits and special characters. (Don't consider space as a special character)

str = input("Input a string: ")
upper, lower, number, special = 0, 0, 0, 0
for i in range(len(str)):
    if str[i].isupper():
        upper += 1
    elif str[i].islower():
        lower += 1
    elif str[i].isdigit():
        number += 1
    else:
        special += 1

print("Letters: ", len(str))
print('Upper case letters:', upper)
print('Lower case letters:', lower)
print('Number:', number)
print('Special characters:', special)

'''
def countCharacterType(str):
 
    # Declare the variable vowels,
    # consonant, digit and special
    # characters
    str = input("Input a string: ")
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0
 
    # str.length() function to count
    # number of character in given string.
    for i in range(0, len(str)):
         
        ch = str[i]
 
        if ( (ch >= 'a' and ch <= 'z') or
             (ch >= 'A' and ch <= 'Z') ):
 
            # To handle upper case letters
            ch = ch.lower()
 
            if (ch == 'a' or ch == 'e' or ch == 'i'
                        or ch == 'o' or ch == 'u'):
                vowels += 1
            else:
                consonant += 1
         
        elif (ch >= '0' and ch <= '9'):
            digit += 1
        else:
            specialChar += 1
     
    print("Vowels:", vowels)
    print("Consonant:", consonant)
    print("Digit:", digit)
    print("Special Character:", specialChar)
 
 
# Driver function.
# str = "geeks for geeks121"
countCharacterType(str)
'''