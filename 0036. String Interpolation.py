#String Interpolation

'''
The process of evaluating a string literal containing one or more
placeholders, yielding a result in which the placeholders are replaced with their
corresponding values.
'''

name = 'Rudra'
age = 28

# greeting = 'My name is ' + name + ' and I am ' + str(age) + ' years old'

greeting = 'I am {age} years old and my name is {name}'.format(name=name, age=age)

print(greeting)