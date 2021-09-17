'''
Can you change the self parameter inside a class to something else
(say 'harry'). Try changing self to 'slf' or 'harry' and see the effects.
'''

class Sample:
    # def __init__(self, name):
    #     self.name = name

    def __init__(harry, name):
        harry.name = name   # yes it will work but if 
    # u will give this code to others who is working on another codebase they will become confused

obj = Sample("Harry")
print(obj.name)

import random
n = int(input())
for i in range(1,n+1):
    p = random.randint(1,5)
    print(p)