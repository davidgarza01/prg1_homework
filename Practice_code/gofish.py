from deck import deck 
from player import players


draw_pile = deck(True)
discard_pile = deck()

draw_pile.fan()

discard_pile.fan()

playercount = int(input("How many people are playing?"))
player = {}
for current_player in range(playercount):
    player[input("Enter your name")] = player()

for current_player in players:
    current_player.increase_score 
    print(''' Which player to you want to ask:
        1) Kirkhoffer 
        2) Spice
        3) Wamsley
        4) Mr.Gold
    ''')
    choice = int(input(">"))
    if(choice == 1):
        Kirkhoffer = input("Kirkhoffer, Do you have a ___")
    elif(choice == 2):
        spice = input(" Spice, Do you have a ___")
    elif(choice == 3):
        wamsley = input("Wamsley, Do you have a ___")
    elif(choice == 4):
        mrgold = input("Mr. Gold, Do you have a ___")
    else:
        print("Invalid ")




