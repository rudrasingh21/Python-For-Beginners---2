#Function takes input and produces a result on the basis of code.

# Makes program easy to handle and reusable.

def fun1():
    return "Hello Function!"

print(fun1())

print(fun1().upper())

print(fun1().lower())

print(len(fun1()))

#NOTE:- if we will not use return and use print,
#  then it will return 'None'

def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('Hi'))

#Default value

def hello_func1(greeting, name='you'):
    return '{},{}'.format(greeting, name)

print(hello_func1('Hi'))

print(hello_func1('Hi', name = 'Rudra'))