## Class vs Static Methods

import csv # to read the CSV file

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # Problem- you don't want to instantiate everytime and assign values. So how to instantiate from a csv file?
    # Answer- We'll use class method.
    
    # in order to convert this to a class method, we need to use a decorator.
    # Decorators in python is just a quick way to change the behavior of that functions that we will 
    # write by basically calling them just before the line that we create our function.
    @classmethod
    def instantiate_from_csv(cls): # the class object itself will be passed as the first parameter always in the background.
        with open('Chapter 10a - OOPs\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float): # this built in fxn will check if the received parameter (num) is an instance of a float or an integer.
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
# to access class methods
Item.instantiate_from_csv()
print(Item.all) # this stores all the instances inside the list

# to access static method
print(Item.is_integer(7)) # 7.8