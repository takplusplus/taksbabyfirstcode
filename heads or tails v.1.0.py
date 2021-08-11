import random
import sys

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
print(result)
if yourchoiceinput == result:
    print("you won")
else:
    print("you loss")
