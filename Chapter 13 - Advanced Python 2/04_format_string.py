# format method is old method and now mostly used f string method

name = "Harry"
channel = "CodeWithHarry"
type = "coding"

# a = f"This is {name}" # use of f string
# a = "This is {}".format(name)
# a = "This is {} and his channel is {}".format(name, channel)
# a = "This is {1} and his {2} channel is {0}".format(name, channel, type)
a = "This is {0} and his {2} channel is {1}".format(name, channel, type)
# a = "This is {} and his {} channel is {}".format(name, channel, type)

print(a)
