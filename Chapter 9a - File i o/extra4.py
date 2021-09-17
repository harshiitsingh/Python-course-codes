'''
4. Write a program to read the contents from a file and count the number of occurrences of
vowels in the content.
'''

with open('vowels.txt') as f:
    str = f.read()

    vowel_count =  0
    for i in str:
        if( i=='A' or i=='a' or i=='E' or i=='e' or i=='I'
            or i=='i' or i=='O' or i=='o'
        or i=='U' or i=='u'):
                vowel_count +=1
        

print('The Number of Vowels in text file :', vowel_count)