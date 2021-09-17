'''
Q.5 Consider a list with 5 different Celsius values.
Convert all the values to Fahrenheit using list comprehension
'''

celsius = [22, 28, 33, 42, 52]

fahr = [e * 9/5 + 32 for e in celsius]
print(fahr)