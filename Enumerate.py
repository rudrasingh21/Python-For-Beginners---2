#Enumerate

#Is a built in function that adds a counter to an iterable.

A = ['once','upon','a','time']

print(list(enumerate(A)))

'''
[(0, 'once'), (1, 'upon'), (2, 'a'), (3, 'time')]
'''

#NOTE:- enumerate adds a counter as you can see above.

#--------------------------
#We can change start counter as well

A = ['once','upon','a','time']

print(list(enumerate(A, start = 10)))

'''
[(10, 'once'), (11, 'upon'), (12, 'a'), (13, 'time')]
'''

#NOTE:- start , starts counter from given counter.

#---------------------------

#enumerate has its own object

print(type(enumerate(A)))

'''
<class 'enumerate'>
'''

#---------------------------

#Using for loop

for index , value in enumerate(A):
    print("Endex Number: " + str(index) + " Value is: " + str(value)+ '\n')
