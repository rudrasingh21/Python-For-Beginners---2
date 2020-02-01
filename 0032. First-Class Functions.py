
#First-Class Functions
'''
A first class citizen(first-class object) in a programming language is an
entity which supports all the operations generally available to other entity.
These operations typically include being passed as an argument, returned from a
function , and assigned to a variable.
'''

def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

square = my_map(square,[1,2,3,4,5,6])

cube = my_map(cube , [1,2,3,4,5,6])

print(square)
print(cube)