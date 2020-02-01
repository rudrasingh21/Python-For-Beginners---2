#Combinations and Permutations
'''
Permutation :- Way to group some value where order does matter.
Combination :- Way to group something where order does not matter.
'''

import itertools

my_list = [1,2,3]

combinations = itertools.combinations(my_list,3)

for c in combinations:
    print(c)

#Output:- (1, 2, 3)
# It will find out only one output as in combination order does not matter.

'''
combinations = itertools.combinations(my_list,3)
(1, 2)
(1, 3)
(2, 3)
'''

#Check below for permutation

permutation = itertools.permutations(my_list , 3)

for p in permutation:
    print(p)

'''
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)

Because Order does matter.
'''