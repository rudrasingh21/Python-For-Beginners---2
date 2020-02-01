#Combinations and Permutations

#Example where we can use Permutation :-

import itertools

word = 'sample'
my_letters = 'plmeas'

permutation = itertools.permutations(my_letters,6)

for p in permutation:
    #print(p)
    if ''.join(p) == word:
        print('Match!')
        break
else:
    print('No Match.')


