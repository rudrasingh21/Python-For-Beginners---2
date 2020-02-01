#Clousres_Part2

def outer_fun(msg):
    message = msg

    def inner_fun():
        print(message)

    return inner_fun

hi_fun = outer_fun('Hi...')
hello_fun = outer_fun('Hello...')

'''
NOTE:-
Each of these variable remembers the values of their 
own variable.  
'''

hi_fun()
hello_fun()