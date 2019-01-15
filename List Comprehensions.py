#Comprehensions

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
  my_list.append(n)
print(my_list)

#Using List Comprihension

my_list_com = [n for n in nums]
print(my_list_com)

############

#I want 'n*n' for each 'n' in nums
my_list1 = []
for n in nums:
  my_list.append(n*n)
print(my_list)

#Using List Comprihension

my_list1_com = [n*n for n in nums]
print(my_list1_com)

#Using MAP and LAMBDA

my_list_lambda = map(lambda n: n*n , nums)
print(my_list_lambda)
for i in my_list_lambda:
    print(i)

#List Comprehensionss more examples:-

# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
  if n%2 == 0:
    my_list.append(n)
print(my_list)

#Usaing a list Comprehensions

my_list_com = [n for n in nums if n%2 == 0]
print(my_list_com)

#Using Filter and LAMBDA

my_list_Filter = filter(lambda n : n%2 == 0 , nums)
print(my_list_Filter)
for i in my_list_Filter: print(i)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
  for num in range(4):
    my_list.append((letter,num))
print(my_list)

#Using List Comprehensions

my_list_com = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list_com)

## Dictionary Comprehensions

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(zip(names, heros))

for (name,heros) in zip(names, heros):print(name,heros)

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

#Dictionary Comprihensions:

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {name:hero for name , hero in zip (names, heros)}
print(my_dict)

# If name not equal to Peter
my_dict = {name:hero for name , hero in zip (names, heros) if name != 'Peter'}
print(my_dict)

#Set Comprehension

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

#Using Set Comprehension

my_set = {n for n in nums}
print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print(i)

#Using Generator Expressions

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)



