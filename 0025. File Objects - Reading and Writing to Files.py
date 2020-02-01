#File Objects - Reading and Writing to Files

'''
Opening a file in reading / writing / append mode
'''

f = open('test.txt','r')

#f = open('test.txt','w')   --write
#f = open('test.txt','r+')  --read and write
#f = open('test.txt','a')   --append

print(f.name)   #will print file name
print(f.mode)   #will give r coz it is in reading mode

f.close()

#another way -- which close file automatically

with open('test.txt','r') as f:
    print(f.read())