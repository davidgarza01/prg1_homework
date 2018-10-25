import random 
players = {}
players["player1"] = input("What is your name you are player 1")
players["player2"] = input("What is your name you are player 2")
scores = {}
less_rounds = 0
min_rounds = 3 
while (less_rounds < min_rounds):
    print("This is round number " + str(less_rounds + 1))
    score = {}
    for player in players.values():
        print("It is your turn", player)
        input("Press enter to roll")
        roll_dice = random.randint(1,6)
        print(roll_dice)
        score[player] = int(roll_dice)
    if (score[players["player1"]] < score[players["player2"]]):
        print(players["player2"], " won this round")
    elif (score[players["player1"]] > score[players["player2"]]):
        print(players["player1"], " won this round")
    elif (score[player["player1"]] == score[player["player2"]]):
        print("It is a tie, try again")
    less_rounds += 1