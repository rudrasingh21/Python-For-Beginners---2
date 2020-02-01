#Closures:-

'''
Basic Note:-
fun():- using () , function executes.
return fun():- executes fun and return it.

return fun :- Just return function without executing it.
'''

def outer_fun():
    message = 'Hi'

    def inner_fun():
        print(message)

    return inner_fun()

my_fun = outer_fun()

#Output :- Hi

##################################

def outer_fun1():
    message = 'Hi'

    def inner_fun1():
        print(message)

    return inner_fun1            #Here we are not executing function , just returning it

my_fun1 = outer_fun1()
print('No Output')
#No output because my_fun1 variable is a function now.
#To check-

print(my_fun1)
#Output:- <function outer_fun1.<locals>.inner_fun1 at 0x0000021BE0F57E18>

print(my_fun1.__name__)         #Outpit:- inner_fun1
#now we can execute this just like any other function
my_fun1()
#output:- Hi

'''
Note:- This is a closure.
A closure is inner function that remembers and has access too, variables in the local scope
in which it was created. Even after the outer function finish executing.
'''