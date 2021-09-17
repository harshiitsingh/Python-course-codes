
def game():
    return 644

score = game()
with open("hiscore.txt") as f:
    # hiscore = int(f.read())
    hiScoreStr = f.read()

if hiScoreStr == '':  # this if condition is for when file will be blank or no score is written in that
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
        
elif int(hiScoreStr)<score:
    with open("hiscore.txt", "w") as f:
        f.write(str(score)) # typecasted into str, coz f.write() takes string not integer