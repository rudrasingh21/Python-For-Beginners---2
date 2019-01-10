# *args and **kwargs
# It allows arbitrary number of positional or keyword arguments.

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

'''
If we dont know how many 
Positional and Keyword arguments will be in program
Then use *args, **kwargs
'''

student_info('Math','Art',name='John',age=22)

'''
OUTPUT:-
('Math', 'Art')                 **args-->tuple , which we passed positional arguments
{'name': 'John', 'age': 22}     **kwargs--> dictonary , with all keywork value
'''

#**********Other way**********

def student_info_new(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ['Math_new','Art_new']
info = {'name_new': 'John_new','Age_new':000}

#student_info_new(courses,info) ---> If we pass like this then we will get wrong results

student_info_new(*courses,**info)

#NOTE:- We have used * to unpack Positional values ,
# and ** to unpack Key word values
'''
Output:-
('Math_new', 'Art_new')
{'name_new': 'John_new', 'Age_new': 0}
'''