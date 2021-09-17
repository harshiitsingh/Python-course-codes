with open("vowels1.txt") as f:
    string = f.read()

def getVowels(word):
    vowels = "aeiouAEIOU"
    print(len([letter for letter in word if letter in vowels]))
    print([letter for letter in word if letter in vowels])

getVowels(string)