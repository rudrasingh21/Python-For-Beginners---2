from my_module import Find_Index,test #--> import specific function
#import my_module

import sys

'''In sys module , sys.path -> 
where path is defined to check path when we import anything'''
courses = ['History','Math','Art','Physics']

index = Find_Index(courses,'Math')
print(index)

print(test)

print(sys.path)

'''
NOTE:-

if your script which you are importing is on some other path,
You can add that path to ---> sys.path

import sys
sys.path.append('user/desktop/...')
'''
#Grab a random value from list of values

import random

Cour = ['Hist','Geo','Maths','Eng']

random_course = random.choice(Cour)

print(random_course)

#Above will random choose any course from Cour

