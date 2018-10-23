import random 

player1 = input("Enter your name, you are player 1 ")
player2 = input("Enter your name, you are player 2 ")

players = [player1 , player2]
scores ={}
print(players)
for x in scores:
    dice = random.randint(1,6)
    scores["turn1player1"] = dice
print(scores[turn1player1])