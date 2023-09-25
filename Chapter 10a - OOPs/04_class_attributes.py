'''
--> Full Name Instance Attributes
--> Class Attributes: that is global and shared among all the instances of the class.
                        It belongs to the class itself. But however, you  can also access this attribute
                        from the instance level as well.

'''

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    
    def __init__(self, name: str, price: float, quantity=0) -> None:
        ## Run validations to the received arguments
        assert price>=0, f"Price {price} is not greater than or equal to zero!"
        assert quantity>=0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        ## Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def calculate_total_price(self):
        return self.price * self.quantity
        
    def apply_discount(self):
        # override an attribute that is belonging to an instance, that can be done by self keyword.
        self.price = self.price * self.pay_rate # or use Item.pay_rate at class level. But best practice is to use at instance level.
    
        
item1=Item("Phone", 100, 5)
print(item1.name)
print(item1.calculate_total_price())

# How to access class attributes?
print(Item.pay_rate) # at class level
print(item1.pay_rate) # at instance level. 
# But how does this work at instance level?
# First the object tries to find the attribute at instance level, if not found, then tries to find at class level.

## Built in Magic Attribute that helps to see all the attributes  that are belonging to that specific object.
## take all attributes and store into a dictionary
## can be used for debugging reasons
print(Item.__dict__) # All attributes at class level
print(item1.__dict__) # All attributes at instance level

item1.apply_discount()
print(item1.price)

# Now suppose discout for another item is different. So changing pay_rate at class level is not a good idea.
item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
