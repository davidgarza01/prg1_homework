print("Give me a number")
number = input(">")
factors_list =[]
for x in range(1, int(number) + 1):
    if (int(number) % x == 0):
        factors_list.append(x)
print(number,"has",len(factors_list),"factors, ","which are", factors_list)

    