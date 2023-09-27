import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # just for example:
    # @property
    # def read_only_name(self):
    #     return "AAA"

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        '''
        return self.name # doing this means we are telling to class 
        that you're going to have a name attribute that is read-only.
        so inside the contructor we are no more allowed to assign/set self.name = name
        and you are only allowed to see this back in whatever instance you will ceate and that is illegal/wrong approach.
        so pythonic way is to add two underscores before the actual name of attribute. Why?
        
        Single underscore -->
        
        Double Underscore --> to prevent the access to those attributes totally outside of the class. 
                            Similar to protected attributes in Java or C#
        '''
        
        print("You're trying to get name")
        return self.__name


    # similarly, there are some properties that help to set the values of the attributes.
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"