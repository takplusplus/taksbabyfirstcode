import random
import sys

print("""\

┌┐░░░░░░░░░┌┐░░░░░░░░░░┌┐░░░░┌┐░░░░
││░░░░░░░░░││░░░░░░░░░┌┘└┐░░░││░░░░
│└─┬──┬──┬─┘├──┐┌──┬─┐└┐┌┼──┬┤│┌──┐
│┌┐││─┤┌┐│┌┐│──┤│┌┐│┌┘░│││┌┐├┤││──┤
│││││─┤┌┐│└┘├──││└┘││░░│└┤┌┐││└┼──│
└┘└┴──┴┘└┴──┴──┘└──┴┘░░└─┴┘└┴┴─┴──┘
┌┐░░░░░░┌───┐░░░░░░░░░░┌┐░░░┌────┐░┌┐░░
││░░░░░░│┌─┐│░░░░░░░░░░││░░░│┌┐┌┐│░││░░
│└─┬┐░┌┐││░│├─┐┌──┬─┬──┤└─┬─┴┤││├┴─┤│┌┐
│┌┐││░│││└─┘│┌┐┤┌┐│┌┤┌─┤┌┐│┌┐││││┌┐│└┘┘
│└┘│└─┘││┌─┐││││┌┐│││└─┤│││└┘││││┌┐│┌┐┐
└──┴─┐┌┘└┘░└┴┘└┴┘└┴┘└──┴┘└┴──┘└┘└┘└┴┘└┘
░░░┌─┘│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░└──┘░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
origninally created 6/25/2021
version 2.0
""")
points = 0
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
        return True
    else:
        print("you loss")
        return False


while 3 > 1:
    if maingame() == True:
        points += 1
    print("your total points is:")
    print(points)

    playercontinue = input("would you like to play again?")
    if playercontinue == "no":
        break
