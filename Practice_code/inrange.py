

def number_in_range(low, high, number):
    if(low < number and high > number):
        return True
    else:
        return False

number1= 1
number10 = 10
number_in_the_range = 4
number_out_range = -5 
number_too_high = 100
isnumberinrange = number_in_range(number1, number10, number_in_the_range)
print(isnumberinrange)
number_in_range(number1, number10, number_out_range)
number_in_range(number1, number10, number_too_high)