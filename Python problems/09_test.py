'''
Write a program that accepts a sentence as input and calculates the number of letters,
digits and special characters. 
(Don't consider space as a special character)
'''
# Q.1
def countCharacterType(str):
    str = input("Enter a string: ")
    vowels, consonant, specialChar, digit, spaces = 0, 0, 0, 0, 0

    for i in range(0, len(str)):
        ch = str[i]
        if ( (ch >= 'a' and ch <= 'z') or
              (ch >= 'A' and ch <= 'Z') ):
            ch = ch.lower()
 
            if (ch == 'a' or ch == 'e' or ch == 'i'
                        or ch == 'o' or ch == 'u'):
                vowels += 1
            else:
                consonant += 1
         
        elif (ch >= '0' and ch <= '9'):
            digit += 1
        elif (ch == ' '):
            spaces += 1
        else:
            specialChar += 1
     
    print("Letters:",len(str))
    print("Digit:", digit)
    print("Special Character:", specialChar)

countCharacterType(str)