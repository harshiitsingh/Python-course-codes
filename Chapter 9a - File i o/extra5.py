'''
5. Write a program to read the contents from a file and count the number of occurrences of
digits, alphabets, special symbols and white spaces.
'''

def counter(fname):
	num_words = 0
	num_lines = 0
	num_charc = 0
	num_spaces = 0
	with open(fname, 'r') as f:
		for line in f:		
			num_lines += 1			
			word = 'Y'					
			for letter in line:
				if (letter != ' ' and word == 'Y'):					
					num_words += 1										
					word = 'N'								
				elif (letter == ' '):										
					num_spaces += 1					
					word = 'Y'
			
				for i in letter:
					if(i !=" " and i !="\n"):
						num_charc += 1
						
	print("Number of words in text file: ", num_words)
	print("Number of lines in text file: ", num_lines)
	print('Number of characters/alphabets in text file: ', num_charc)
	print('Number of White spaces in text file: ', num_spaces)
	
if __name__ == '__main__':
	fname = 'vowels.txt'
	try:
		counter(fname)
	except:
		print('File not found')
