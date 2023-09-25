# Suppose our shop is going to be at large scale. Then how to see all the list of items/instances present in our store.

'''
Watch: Python Magic Methods | Differences between __str__ to __repr__ --> https://www.youtube.com/watch?v=FIaPZXaePhw
--> https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
'''

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

    # Magic Method: __repr__ means representing your objects
    # But why working so hard to just represent the objects? Because it's best practice to do that and python documentation.
    def __repr__(self):
        # return "Item"
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

for instance in Item.all:
    print(instance.name)