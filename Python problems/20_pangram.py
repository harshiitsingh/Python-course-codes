
def checkPangram(sentence):
    for i in sentence:
        if (ord('a') <= ord(i) <= ord('z')) or (ord('A') <= ord(i) <= ord('Z')):
            return True
        else:
            print(i)
sentence = input("Enter a sentence: ")
if checkPangram(sentence) == True:
    print("A pangram")
else:
    print("Not a pangram")

# to check pangram 

def checkPangram(str):
    if len(set('abcdefghijklmnopqrstuvwxyz') - set(str.lower())) == 0:
        return True
    return False

sentence = input("Enter a sentence to check for Pangram: ")
if(checkPangram(sentence)):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
    print("Hence, the missing letters are: ")
    print(set('abcdefghijklmnopqrstuvwxyz')^set(sentence.lower()))