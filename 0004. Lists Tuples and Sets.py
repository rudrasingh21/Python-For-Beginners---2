courses = ['History','Maths','English','Computer']

print(courses)
print(type(courses))
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[3])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

#Adding in last in the list
courses.append('Art')

print(courses)

#Adding at specific location - This will add at starting - Will not override.

courses.insert(0,'Physics')

print(courses)

#Using Extend Method :- to add one list to another list

courses1 = ['History1','Maths1','English1','Computer1']

print(courses1)

courses.extend(courses1)

print(courses)

#Reverse    -- To print it in reverse order.

courses.reverse()

print(courses)             # '''It riverses whole list '''

#Sort       -- To sort list

num = [1,3,2,9,6]
courses.sort()
print(courses)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

#sorted function   -- another way for sorting

courses1 = ['History1','Maths1','English1','Computer1']

sorted_func = sorted(courses1)

print(sorted_func)

# min , max , sum function      -- min function to get minimum.

print(min(num))
print(max(num))
print(sum(num))

#find out index in list

courses = ['History','Maths','English','Computer']
print(courses)
print(courses.index('Computer'))

print('Art' in courses)
print('History' in courses)

#Use of for loop for list

for i in courses:
    print(i)

#Accessing Index using for loop

for index , course in enumerate(courses, start = 0):    #by default start =0 , we can change this too
    print(index,course)

#Seperate String join

course_str = ' - '.join(courses)
print(course_str)
'''OutPut:- History - Maths - English - Computer'''

#split function - to Split this string

new_list = course_str.split(' - ')
print(new_list)
'''OutPut:- ['History', 'Maths', 'English', 'Computer']'''

# List are mutable and Tuples are not

#So If you need something you need to modify , use List otherwise use Tuple

#set
#contails only unique values
#Are unordered

set_example = {'maths','physics','science','history'}   #Only gives unique values in output

print(set_example)

print( 'maths' in set_example)

#will through True , we also can use this in tuples and List , but SET are OPTIMIZED for this

# Set can do intersection

set_example = {'maths','physics','science','history'}
set_example1 = {'maths','srt','bio','hindi'}

print(set_example.intersection(set_example1)) # will give you only common

#difference

print(set_example.difference(set_example1)) #Will show only unique set_examplt

print(set_example1.difference(set_example)) #Will show only unique set_example1

#union

print(set_example.union(set_example1))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()




'''
---------
Output:-
---------
['History', 'Maths', 'English', 'Computer']
<class 'list'>
4
History
Computer
Computer
['History', 'Maths']
['History', 'Maths']
['English', 'Computer']
['History', 'Maths', 'English', 'Computer', 'Art']
['Physics', 'History', 'Maths', 'English', 'Computer', 'Art']
['History1', 'Maths1', 'English1', 'Computer1']
['Physics', 'History', 'Maths', 'English', 'Computer', 'Art', 'History1', 'Maths1', 'English1', 'Computer1']
['Computer1', 'English1', 'Maths1', 'History1', 'Art', 'Computer', 'English', 'Maths', 'History', 'Physics']
['Art', 'Computer', 'Computer1', 'English', 'English1', 'History', 'History1', 'Maths', 'Maths1', 'Physics']
[1, 2, 3, 6, 9]
[9, 6, 3, 2, 1]
['Computer1', 'English1', 'History1', 'Maths1']
1
9
21
['History', 'Maths', 'English', 'Computer']
3
False
True
History
Maths
English
Computer
0 History
1 Maths
2 English
3 Computer
History - Maths - English - Computer
['History', 'Maths', 'English', 'Computer']
{'science', 'history', 'physics', 'maths'}
True
{'maths'}
{'science', 'history', 'physics'}
{'bio', 'srt', 'hindi'}
{'physics', 'maths', 'srt', 'history', 'hindi', 'bio', 'science'}
'''