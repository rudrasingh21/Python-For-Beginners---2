#Idempotence

'''
The property of certain operations in mathematics
and computer science, that can be applied multiple
times without changing the result beyond the initial
application.

f(f(x) = f(x)

Meaning is :-
if we have function f
and parameter x

Then Result will be f(x)

So if you pass function f again , that will equal to result of f(x)

'''

# Below example is not IDEMPOTENCE:-

def add_ten(num):
    return num +10

print(add_ten(5))
#Result:- 15
print(add_ten(add_ten(5)))
#Result:- 25

#above is not IDEMPOTENCE.

########## Another Idempotence Example

print(abs(-10))

print(abs(abs(-10)))

#above is IDEMPOTENCE.

'''
HTTP METHODS

GET         <url>/users/123 (Idempotent)
PUT                         (Idempotent)
POST                        (not Idempotent)
DELETE                      (Idempotent)

SO in HTTP url , you can reload page n number of times , 
you will get same result.
'''
