'''
Problem 1
'''
people = int(input("How many people are attending to the campfire?"))
if (people == 1):
    print("Just you then?")
if (people == 2):
    print("Bring marshmellows, please")
if (people >= 3):
    print("More than 3 is a crowd")
if(people >= 7):
    print("Party")
if (people < 0):
    print("Which dimension have you entered?")
'''
Problem 2 
'''
speed_limit5 = 55
speed_limit15 = 65
speed = int(input(">"))
speed_limit = 50
license_loss= 50 * 2
bdaycop = str(input("Is it your birthday?"))
bday = "Yes"
if(speed < speed_limit):
    print("No ticket")
if(bdaycop == bday):
    print("Happy birthday to you, happy birthday dear David, Happy birthday to you")
    speed = speed - 5


if(speed > speed_limit and speed < speed_limit5):
    if(bdaycop == bday):
        speed = speed - 5
        print("warning")

if(speed > speed_limit5 and speed < speed_limit15):
    if(bdaycop == bday):
        speed = speed - 5
        print("Small Ticket")

if(speed > speed_limit15 and speed < license_loss):
    if(bdaycop == bday):
        speed = speed - 5
        print("Big ticket")

if(speed > license_loss):
    if(bdaycop == bday):
        speed = speed - 5
        print("Immediate license loss")
