#Memoization:-

'''
Memoization is a technique of recording the intermediate results so that
it can be used to avoid repeated calculations and speed up the programs.
It can be used to optimize the programs that use recursion.
In Python, memoization can be done with the help of function decorators.
'''
import time

ef_cache = {}

def expencive_fun(num):
    if num in ef_cache:
        return ef_cache[num]

    print("Computing {}....".format(num))
    time.sleep(1)
    result = num * num
    ef_cache[num] = result
    return result

result = expencive_fun(4)
print(result)

result = expencive_fun(10)
print(result)

result = expencive_fun(4)
print(result)

result = expencive_fun(10)
print(result)