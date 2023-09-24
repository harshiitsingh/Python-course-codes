## Special Variable __name__

'''
- What is the starting point of execution of code?
- What is a special variable in Python?
- _name_ variable in python
- How the name variable works in Python?


#1
- _main_  is the starting point of the python. 
- The first module name is always main and the code starts from main.
- _name_ is a variable name that return the __main__.
- name_ is a built-in variable that evaluates the name of the current module.
- The value of the name changes as per the place where it is used, so that's why it is known as a variable.
- If you are an individual file or module, then the name will return main. 
- If you are importing another module containing the name variable in any file, then the name variable will return the name of that module.
OR, 
- If you are running a file as a main and using a named variable in it, then it will print the main.
- But if you are printing a name that is imported as a module in another file, then it will print the module name.

#2
- The use of a function with the name variable helps the interpreter in checking if it's parsing the currently executed script, or if it's temporarily parsing another external script. 
 if _name_ == "__main__":
This statement helps us to control the behaviour of different parts of the program.
- It chooses the number of lines of codes that can be executed from the external script as well as the currently executed script depending on the scenarios.
'''

# print("Hello " + __name__)

import demo

print("Its Time to Calculate")
# demo.main()

'''
- main () function in Python
- How special variable is executed with main()?
- How to restrict the execution of statements present inside the main() function?
- Starting point of execution of code


#1
- When we define a function, then we will have to call that function also to print or perform something.
- main() is the starting point of execution.
- main() function will also work only when we call the main() function. 
- From the main() function, we can call all other functions that are available in the code.
- When you import the library or a module, it will execute all statements present inside it.
- And if it contains the callable main() function, then main() will call all functions present in the imported module.
- We can also call the main() function only when we want to execute the particular file as a Standalone program.
- We can control the execution flow of main() by using:
 if _ name_  == _main()_
- So by using this, some set of statements will be executed only when we call the __name__.
'''