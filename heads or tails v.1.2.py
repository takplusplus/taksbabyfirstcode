import random
import sys

def maingame():

    playerchoices = ["heads", "tails"]

    yourchoiceinput = input('heads or tails? type it\n')
    yourchoiceinput = yourchoiceinput.lower()
    if not yourchoiceinput in playerchoices:
        print("you have to type heads or tails")
        sys.exit(1)

    def roll():
        diceroll = random.choice(playerchoices)
        return diceroll

    result = roll()

    if yourchoiceinput == result:
        print("you won")
    else:
        print("you loss")

storeoftimes = ["1","2","3"]
for i in storeoftimes:
    maingame()
    playercontinue = input("would you like to play again?")
    if playercontinue == "no":
        break
