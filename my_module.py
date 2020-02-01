print("Imported my Module..")

test = 'Test String'

def Find_Index(to_search, target):
    '''find the index of a value in a sequence'''
    for i , value in enumerate(to_search):
        if value == target:
            return i

    return -1