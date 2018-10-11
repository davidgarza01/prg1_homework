'''
a strong number is defined as a number thas has the sum of the factorial of each digit is equal to its original number 

'''

for number_to_check in range(10000001):
    snumber = str(number_to_check)

#get all of the digits (split)
    digits = list(snumber)
    sum = []
#calculate factorial 
    for digit in digits:
        factorial = 1
        for number in range(1,int(digit)+1):
            factorial = number * factorial
        sum.append(factorial)

#add all factorial together 
    final_factorial = 0
    for number in sum:
        final_factorial += number    
#check if the sum is same as the original       
    if(final_factorial == int(snumber)):
        print(snumber, "this number is strong")

