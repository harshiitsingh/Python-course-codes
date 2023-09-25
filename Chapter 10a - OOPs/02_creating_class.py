class Item:
    # pass
    
    # # anything created with name def is called as function, but function created inside the class is called as METHODS.
    # def calculate_total_price(self): # self in python will pass the object itself as the first argument every time,
    #     # that's why we are not allowed to create methods that will never receive parameters, we at least need to pass 'self'.
        
    #     # try runnig code by removing self, you'll get error
    #     pass
    
    def calculate_total_price(self, x, y):
        return x*y
        
item1 = Item() # creating instance of the class Item

# random_str = "4" is similar to random_str = str("4") of str class

# Let's assign some attributes to the class
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

# random_str = "aaa"
# print(random_str.upper()) ## there is upper method of str class
# So how to design some methods that are going to be allowed to execute on our instances? -> Inside our class

item2 = Item()
item1.name = "Laptop"
item1.price = 1000
item1.quantity = 3

# item1.calculate_total_price() # no parameters, so object will be passed itself.
print(item1.calculate_total_price(item1.price, item1.quantity))
print(item2.calculate_total_price(item2.price, item2.quantity))