

def find_minimum_value(values):
    
    
    
    
    
    special_value = values[0]
    for value in values:
        if (value < special_value):
            special_value = value
    return special_value

def find_position(values,element):

    index = 0 
    for value in values:
        if(value == element):
            return index
        index += 1
    pass

def selection_sort(values):

    for value in values:
        smallest_value = find_minimum_value(values)
        position = find_position(values,smallest_value)
        values[position] = smallest_value
        count += 1
    return values

unsorted = [243,-10,4,3,2,3]
print(selection_sort(unsorted))

