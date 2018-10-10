print("please enter 5 numbers separated by a space")
numbers = input("Write 5 numbers")
numbers_split = numbers.split(" ") 
if(len(numbers_split)==5):
    sum = 0 
    for nx in number_split:
        x = float(nx)
        sum += x

    print(sum, "is not your final score")

    score = 0
    for swicked in numbers:
        wicked = float(swicked)
        if(wicked == 13.0):
            score += 100
        elif(wicked ==7.0):
            score += 30 
        elif(wicked %2 == 1):
            score += wicked * 2 
        elif(wicked %2 == 0):
            score += wicked/2
        else: 
            print("not valid")

    print(score, " is yout final score")
else: 
    print("enter the numbers again")
