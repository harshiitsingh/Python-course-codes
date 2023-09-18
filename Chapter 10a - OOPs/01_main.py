item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print(type(item1)) # str
print(type(item1_price)) # int
print(type(item1_quantity)) # int
print(type(item1_price_total)) # int

# We can see from the above prints output, they are showing as class str/int
# So in Python, each datatype is an object that has been instantiated earlier by some class.
# So item1 variable has been instantiated from a string type of class.

# If we want to tell python that we want to create a datatype of our own, it will allow
# us to write a code that we can reuse in the future easily if needed.