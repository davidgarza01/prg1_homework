#dice roll game
import time
print('''
Greetings Professor Falken
Shall we play a game?
''')


while True: 
    y_n = input('''
    1) Chess
    2) Dice Roll
    3) Checkers
    4) Global Thermonuclear War
    >>> ''')
    if (y_n != "2") :
        print("How about a nice game of dice?")
        time.sleep(1)
    elif (y_n == "2") :
        print ("A good choice")
        time.sleep(1)
        break
y_n = 0
players={}
players ["player_1"] = input("Player 1, what is your name? > ")
players ["player_2"] = input("Player 2, what is your name? > ")

scores = {}
scores[players["player_1"]] = 0
scores[players["player_2"]] = 0
time.sleep(1)


round_score = 0
import random
desired_rounds = 3
while (round_score < (desired_rounds)) :
    print ('''
    Round #''' + str(round_score + 1) + '''
    ''')
    player_score = {}
    for player in players.values():
        player_score[player] = 0
        print(player + ", it is your turn to roll")
        input("Enter to roll...")
        score = random.randint(1,6)
        time.sleep(1)
        print("rolling")
        time.sleep(1.5)
        print("your roll was " + str(score))
        scores[player] += int(score)
        player_score[player] = int(score)
        time.sleep(1)
    if player_score[players["player_1"]] > player_score[players["player_2"]] :
        print(players["player_1"] + " is the round winner with " + str(player_score[players["player_1"]]) + " points!")
    elif player_score[players["player_2"]] > player_score[players["player_1"]] :
        print(players["player_2"] + " is the round winner with " + str(player_score[players["player_2"]]) + " points!")
    elif player_score[players["player_1"]] == player_score[players["player_2"]] :
        print("It is a tie!")
    else : 
        print("404 - data not found")

    round_score += 1

time.sleep(1)
if scores[players["player_1"]] > scores[players["player_2"]] :
    print(players["player_1"] + " is the game winner with " + str(scores[players["player_1"]]) + " points!")
elif scores[players["player_2"]] > scores[players["player_1"]] :
    print(players["player_2"] + " is the game winner with " + str(scores[players["player_1"]]) + " points!")
elif scores[players["player_1"]] == scores[players["player_2"]] :
    print("It is a tie!")
else : 
    print("404 - data not found")
for player in players.values() :
    print (player + ", would you like to play to best of " + str(round_score +2))

    time.sleep(1)

    y_n += int(input("select yes (1) or no (2) > "))

if y_n == 2 :
    print ("A good choice.")
if y_n != 2 :
    print ('''
    A strange game
    the only way to win is not to play
    ''')
while y_n == 2 :
    while (round_score < (desired_rounds + 2)) :
        print ('''
        Round #''' + str(round_score + 1) + '''
        ''')
        
        for player in players.values():
            
            print(player + ", it is your turn to roll")
            input("Enter to roll...")
            score = random.randint(1,6)
            time.sleep(1)
            print("rolling")
            time.sleep(1.5)
            print("your roll was " + str(score))
            scores[player] += int(score)
            time.sleep(1)
            if player_score[players["player_1"]] > player_score[players["player_2"]] :
                print(players["player_1"] + " is the round winner with " + str(player_score[players["player_1"]]) + " points!")
            elif player_score[players["player_2"]] > player_score[players["player_1"]] :
                print(players["player_2"] + " is the round winner with " + str(player_score[players["player_2"]]) + " points!")
            elif player_score[players["player_1"]] == player_score[players["player_2"]] :
                print("It is a tie!")
            else : 
                print("404 - data not found")
        round_score += 1
    time.sleep(1)
    if scores[players["player_1"]] > scores[players["player_2"]] :
        print(players["player_1"] + " is the game winner with " + str(scores[players["player_1"]]) + " points!")
    elif scores[players["player_2"]] > scores[players["player_1"]] :
        print(players["player_2"] + " is the game winner with " + str(scores[players["player_1"]]) + " points!")
    elif scores[players["player_1"]] == scores[players["player_2"]] :
        print("It is a tie!")
    else : 
        print("404 - data not found")
    for player in players.values() :
        print (player + ", would you like to play again?")

        time.sleep(1)

        y_n += int(input("select yes (1) or no (2) > "))

    if y_n == 2 :
        print ("A good choice.")
    if y_n != 2 :
            print ('''
            A strange game
            the only way to win is not to play
            ''')
