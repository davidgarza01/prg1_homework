numbers = []
numbers_list = input("Enter a list of numbers separated by a comma")
numbers_split = numbers_list.split(",")
numbers.append(numbers_list)
#problem 1 
def swap (a,b):
    a = b
    b = a 
    return(a,b)

#problem 2
def bubble(items):
    itemfound = False
    index = 0 
    while(not itemfound and index < (len(items))):
        if index-1 > 0 and items[(index)-1] > items[index]:
            swap_items = swap(items([index - 1]), items[index])
        index += 1
    return True, False

#problem 3
def bubble_sort (items):
    bubble_sorted  = bubble(items)
    while bubble_sorted == False :
        bubble_sorted = bubble(items)

bubble_sort(numbers_list)
print(numbers_list)