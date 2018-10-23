print("Give me some numbers!")
numbers = input(">")
numbers_list = numbers.split(" ")
print("done")
max_number = 0
for number in numbers_list:
    inumber = int(number)
    if(max_number < inumber):
        max_number = inumber
print("The largest number is ", max_number)
