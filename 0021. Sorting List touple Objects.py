#Sorting List  , Touple and Objects

#Sorting List

li = [8,3,6,1,9,6,8,9,0]

#s_li = li.sort() -- this is wrong :- output will be None

s_li = sorted(li)

#or

li.sort()
print("Sorted List is : ",s_li)
print("Using other way sorted List is : ",li)

#Sorting List in desc order

li = [8,3,6,1,9,6,8,9,0]

s_li = sorted(li , reverse=True)

#or

li.sort(reverse=True)
print("\nSorted List is : ",s_li)
print("Using other way sorted List is : ",li)


#Sorting -ve values in List

li = [-6,-5,-4,0,3,1,2]

#to sort this we need abs value

s_li = sorted(li, key=abs)
print(s_li)
#**********************************

#Sorting tuple

li = (8,3,6,1,9,6,8,9,0)

s_li = sorted(li)

#the output is a list
print("\nSorted Tuple is : ",s_li)

#***********************************

#Sorting Dict

di = {'name':'rudra', 'job':'Engineer','age':'None','os':'mac'}

s_di = sorted(di)

print("\nSorted Dict is: ",s_di)

#**********************************

class Employee1:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${}'.format(self.name, self.age, self.salary)

emp_1 = Employee1('Rudra', 27, 500)
emp_2 = Employee1('Apoorv', 25, 600)

print(emp_1)    # because of __repr__ function it  will return value

print(emp_1.name)
print(emp_2.name)

employees = (emp_1,emp_2)
print(employees)

#sorting

#s_employees = sorted(employees)

#print(s_employees) this will give error if we will not function e_sort

def e_sort(emp):
    return emp.salary
    #or return emp.name
    #or return emp.age

s_employees = sorted(employees, key=e_sort, reverse=True)

print(s_employees)

'''
#NOTE:
        Insted using function we only can use lambda function
        
        key = lambda e:e.name
'''

'''
NOTE:   
        Use attergetter:-
        from operator import attergetter
        key= attergetter('age')
'''