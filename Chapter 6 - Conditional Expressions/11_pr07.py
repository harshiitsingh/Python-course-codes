# Q.7 Write a program to find out whether a given post is talking about "Harry" or not.
# any type of harry either in lower or upper case e.g. - Harry, haRRy,etc

comment = input("Enter your post: ")
b = comment.lower()
if 'harry' in b:
    print('This post is about harry')
else:
    print('This post is not about harry')