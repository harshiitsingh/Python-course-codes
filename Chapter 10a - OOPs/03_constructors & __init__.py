# Problem: In previous 02 file, we have hardcoded the attributes (name, price, quantity)
# by using dot, that should be avoided to create those attributes hard coded for each of the instances.

# Solution:-
'''
Constructor (__init__): Using this, objects will be instantiated with the attributes automatically.
    Constructors are generally used for instantiating an object. 
    The task of constructors is to initialize(assign values) to the data members 
    of the class when an object of the class is created. In Python the __init__() method 
    is called the constructor and is always called when an object is created.
    
Syntax of constructor declaration : 
    def __init__(self):
        # body of the constructor
        
--> Overloading not supported

--> Magic Methods

'''

class Item:
    
    # Validate/mention the datatype, so that name is not passed as integers and price as strings
    # name: object reference of class str, will accept only strings
    # no need to specify the typing of quantity, becoz we passed a default value of integer, already marked this parameter as to integer always. 
    def __init__(self, name: str, price: float, quantity=0) -> None: # parametrised constructor
        # print("I am Constructor")
        # print(f"An instance created: {name}")
        
        ## Run validations to the received arguments:-
            # i.e., you also need to validate that you never get a negative value of price and quantity, so we use assert statements.
            # assert is a statement keyword that is used to check if there is a match between what is happening to your expectations.
        assert price>=0, f"Price {price} is not greater than or equal to zero!" # can also add a msg
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        
        ## Assign to self object
        self.name = name # dynamically assign an attribute to an instance from this magic method
        self.price = price
        self.quantity = quantity
        
    
    def calculate_total_price(self):
        # return x*y
        return self.price * self.quantity # we have already assigned those attributes, once the instances has been created, 
        # means we have access to those attributes through how the methods that we are going to add here in this class in the future
        
        

item1=Item("Phone", 100, 5)
print(item1.name)

# item1.has_numpad = False # can add more attributes after you instantiate the instances (outside the constructor)

print(item1.calculate_total_price())