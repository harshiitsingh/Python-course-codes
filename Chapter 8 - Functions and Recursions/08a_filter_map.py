## Lambda, Filter, Map and Reduce

'''
- Filter Map and Reduce in Python
- Use of filter(), map() and reduce() functions
- How lambda function can be used with filter map and reduce
- Syntax of Filter, Map and reduce function
- Difference between filter(), map() and reduce() functions


#1
- Lambda function can be used with these three functions:
1. filter()
2. map()
3. reduce()

#2
- filter() function will take a list and do filtering and give values.
- filter() takes a sequence and also returns a sequence.
- filter() function takes two arguments: function and iterable.
    filter(func, iterable)
- We have to give the definition of a function that we have passed as a condition in an argument.
- The defined function should return a value of either True or False based on the condition.
- Then, filter() will take the value that is returned by the defined function and does perform filtering based on this value.
- In the defined function, we need only two things i.e, a variable and an expression. So, we can also use the lambda function instead of using the normal function to define the condition for a filter.
- Lambda reduces the number of lines of code and makes it more precise.
- Filter() simply returns the iterable passed to it. 

#3
- map() function is used when we want to change the value of every element of a list.
- map() function also takes two arguments i.e., a function and an iterable.
 map(func, *iterables)
-  To get the result as a list, the built-in list() function can be called on the map object.
- We have to define a function that we have passed as a condition in an argument.
- The defined function should return any value. 
- The lambda function can also be used in an argument as a function instead of defining the normal function for the logic.
- map() function returns a list. The function returns a map object which is a generator object.

#4
- reduce() function is used to reduce the number of values from a list.
- reduce() function belongs to a module known as functools.
- We have to import the module functools from the library to use the reduce function.
- reduce() also take two arguments i.e., a function and a sequence.
 reduce(func, iterable[, initial])
- We have to give the definition of a function that we have passed as a condition in an argument.
- The lambda function can also be used in an argument as a function instead of defining the normal function for the logic.


--> https://www.learnpython.org/en/Map,_Filter,_Reduce
'''

from functools import reduce

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2,evens))
print(doubles)

sum = reduce(lambda a,b : a+b,doubles)

print(sum)