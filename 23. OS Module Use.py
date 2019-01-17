#OS Module Use

import os

print(dir(os))

'''
will show all of the attribute and methods in this module
'''

#For current working dir
print(os.getcwd())

#Changing Dir
os.chdir('D:\Study\Hadoop\Python')

#cwd got changed now

print(os.getcwd())

print(os.listdir())

#Creating Dir

#for creating dir at cwd
os.mkdir('test')

#for creating recursive dir at deep down level
os.makedirs('test/test1/test2')

'''
mkdir:- Will create dir only at cwd 
makedirs:- Will create all root and sub dir(tree) if not exists 
'''

#remove dir

os.rmdir('test')

os.removedirs('test/test1/test2')

'''
rmdir:- will remove only dir at cwd
removedirs:- will del all intermediate dir
'''


#Renaming files

os.rename('original.text','new.text')

#eg:-

os.rename('test.text','demo.text')

#Get all Information of a file

print(os.stat('demo.text'))

'''
st_size
st_mtime
st_ctime
etc
'''

#going all the dir and sub dir from cwd

for dirpath , dirnames , filenames in os.walk('D:\Study\Hadoop\Python'):
    print('current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)

#checking dir name and base name

#this will give you basename like 'test.text'

print(os.path.basename('/tmp/test.text'))

#this will give you dir name like '/tmp'

print(os.path.dirname('/tmp/test.text'))

#if you want both of it like ('/tmp','test.text')

print(os.path.split('/tmp/test.text'))

#check if path exist - you will get like True or False

print(os.path.exists('/tmp/test.text'))

#check if it is file or dir - will return True or False

print(os.path.isfile('/tmp/fgthdh'))

print(os.path.isdir('/tmp/fhghf'))

#Taking file name without extensions-for splitting filename and extension

print(os.path.splitext('/tmp/test.text'))

#output:- ('/tmp/test','.text')

