#Combinations and Permutations

#Problem when Combination is useful:-
'''
How many group of 3 you can take from list that are equal to 10.
'''

import itertools

my_list = [1,2,3,4,5,6]

combination = itertools.combinations(my_list,3)
permutation = itertools.permutations(my_list,3)

'''
Question:-
How many group of 3 you can take from list that are equal to 10 where order does not matter.
'''

print([result for result in combination if sum(result) == 10])

'''
Result:- [(1, 3, 6), (1, 4, 5), (2, 3, 5)]
'''


'''
Question:-
How many group of 3 you can take from list that are equal to 10 
where ORDER MATTERs.
'''

print([result for result in permutation if sum(result) == 10])

'''
Result:- [(1, 3, 6), (1, 4, 5), (1, 5, 4), (1, 6, 3), (2, 3, 5), (2, 5, 3), (3, 1, 6), (3, 2, 5), (3, 5, 2), (3, 6, 1), (4, 1, 5), (4, 5, 1), (5, 1, 4), (5, 2, 3), (5, 3, 2), (5, 4, 1), (6, 1, 3), (6, 3, 1)]
'''