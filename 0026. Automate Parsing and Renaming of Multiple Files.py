#Automate Parsing and Renaming of Multiple Files

import os

os.chdir('D:\Study\Hadoop\Python\Cory_Schafer youtube videos')
print(os.getcwd())

for f in os.listdir():
    #print(f)                   #print all file/folders of file
    #print(os.path.splitext(f))  #will split file name and ext
    file_name , file_ext = os.path.splitext(f)
    #print(file_name)           #will print filename only
    #print(file_name.split('-')) #will split file name with space
    f_title , f_topic  = file_name.split('-')
    #print(f_topic)
    f_title=f_title.strip()     #removing whitespaces
    f_topic=f_topic.strip()
    file_ext=file_ext.strip()
    #we can use f_title.strip()[1:] to remove 1st char from f_title
    #Fill Zero like 01 , 02 insted of 1 ,2
    #f_title.strip()[1:].zfill(2)
    #Reformat it again
    #print('{}-{}{}'.format(f_topic,f_title,file_ext))
    new_name = '{}-{}{}'.format(f_topic,f_title,file_ext)
    os.rename(f, new_name)

'''
import os

os.chdir('/path/to/files/')

# Am I in the correct directory?
# print(os.getcwd())

# print(dir(os))

# Print all the current file names
for f in os.listdir():
    # If .DS_Store file is created, ignore it
    if f == '.DS_Store':
        continue

    file_name, file_ext = os.path.splitext(f)
    # print(file_name)

    # One way to do this
    f_title, f_course, f_number = file_name.split('-')

    # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    # Need to remove whitespace
    f_title = f_title.strip()
    f_course = f_course.strip()
    # f_number = f_number.strip()

    # Want to remove the number sign?
    # f_number = f_number.strip()[1:]

    # One thing I noticed about this output is that if it was sorted by filename
    # then the 1 and 10 would be next to each other. How do we fix this? One way we can fix this is to pad
    # the numbers. So instead of 1, we'll make it 01. If we had hundreds of files then this would maybe need to be 001.
    # We can do this in Python with zfill
    f_number = f_number.strip()[1:].zfill(2)

    # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    # You have the power to reformat in any way you see fit
    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

    os.rename(fn, new_name)


# print(len(os.listdir()))
'''