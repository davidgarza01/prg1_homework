'''
wite a function that will return a list with only the unique values

function name : make_unique
parameters: list
returns: list
'''
def make_unique(values): 
    unique = []
    for value in values:
        if(not value in unique):
            unique.append(value)
    return unique

print(make_unique(input( "Enter vakues separated by a comma").split(",")))
