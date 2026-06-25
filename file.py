f = open("basics/file.txt")
data = f.read()
print(data)
f.close()

#File write 
string = "Pankaj Jajim"
f = open("basics/myfile.txt", "w")

f.write(string)
f.close()


# File readline

f = open("basics/file.txt.", "r")
line1 = f.readline()
line2 = f. readline()
f.close()

# Game() function

import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 62)
    #Fetch the hiscore
    with open("basics/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore == ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score: {score}")
    if(score>hiscore):
        #write this hiscore to the file
        with open("basics/hiscore.txt", "w") as f:
            f.write(str(score))
    
    return score
game()

