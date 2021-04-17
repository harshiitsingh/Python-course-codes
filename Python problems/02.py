# Write a Python program to test whether a passed letter is a vowel or not.

a = input("Enter a letter/character: ")
if a in 'aeiouAEIOU':
    print(f"{a} is a vowel")
else:
    print(f"{a} is not a vowel")

# or
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(is_vowel('c'))
# print(is_vowel('e'))