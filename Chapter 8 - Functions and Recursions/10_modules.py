## Modules

'''
- What is a module in Python?
- Use of module 
- How to create a module in Python?
- Advantages of modules
- Steps to add a separate module
- Different ways to import a module


#1
- Debugging simply means removing bugs.
- The concept of modules is used when instead of writing a big software in one file, we will break it down into small parts.
- A module is a file containing Python definitions and statements. It can consist of variables, functions, classes, etc.
-  We have to import a module to use the defined functions in it.
- Module name is the file name with the extension .py.
- Any number of modules can be created and we can also import them into one file.
- Definitions from a module can be imported into other modules or the main module also.
- We have to import the module to use its definitions in the code. When the interpreter encounters an import statement, it imports the module if the module is present in the search path.
- There are some in-built modules present inside python. 
- We can also define our modules and use them in code, and they are known as user-defined modules. 

#2
Advantages of Modules:-
- If we want to change anything in one module then that change will not reflect in any other module.
-  Reuse the same modules in different projects that have similar features.

#3
Steps to add a separate module:-
1. New - Python File
2. Write the name of a new Python File ( name of a module)

#4
Different ways to import a module:-
1. import module_name   (Definitions of all functions can be accessed by using module_name)
2. from module_name import function_name    ( We can use the definition of a particular function)
3. from module_name import *   ( Definition of all functions can be used)

'''
# --> https://stackoverflow.com/questions/4099975/difference-between-a-module-library-and-a-framework

from Calc import *

a = 9
b = 7

c = sub(a,b)

print(c)