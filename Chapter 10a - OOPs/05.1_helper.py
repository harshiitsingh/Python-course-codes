# When to use class methods and when to use static methods ?

class Item:
    @staticmethod
    def is_integer(): # not mandatory, can pass self or num.
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        '''
    @classmethod
    def instantiate_from_something(cls): # cls is the mandatory parameter to pass.
        '''
        This should also do something that has a relationship
        with the class, but usually, those are used to
        manipulate different structures of data to instantiate
        objects, like we have done with CSV.
        
        We can also use JSON or YAML file.
        
        Class Methods are great of helpful if you look to
        instantiate hundreds of objects on your program.
        '''

# THE ONLY DIFFERENCE BETWEEN THOSE:
# Static methods are not passing the object reference as the first argument in the background!


# NOTE: However, those could be also called from instances. As shown below:
item1 = Item()
item1.is_integer()
item1.instantiate_from_something()
# I have never saw a reason to call a static method or a class method from the instance level.