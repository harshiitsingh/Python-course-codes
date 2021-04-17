# SNAKE, WATER, GUN GAME    or   ROCK PAPER SCISSORS

import random

def gameWin(comp,you):
    if comp == you:   # means tie
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer Turn : Snake(s) Water(w) or Gun(g) ?")
randNo = random.randint(1,3)
# print(randNo)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo ==3:
    comp = 'g'

# a = input("Player 1 Turn : Snake(s) Water(w) or Gun(g) ?")
# b = input("Player 2 Turn : Snake(s) Water(w) or Gun(g) ?")

you = input("Your Turn : Snake(s) Water(w) or Gun(g) ?")
a = gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")