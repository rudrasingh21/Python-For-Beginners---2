#CSV Module - How to Read, Parse, and Write CSV Files

import csv

with open('name.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #next(csv_reader)   will iterate to next

    #above is opening file , and iterate to next line

    #below is reading file line by line

    '''for line in csv_reader:
        #print(line)    printing all columns
        print(line[2])'''

    #Below is open a file to write

    with open('new_names.csv','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        #reading from reader and writing to writer
        for line in csv_reader:
            csv_writer.writerow(line)

'''
Dictionary Reader:- Will give you (key:value)

with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for line in csv_reader:
        print(line)
        
        or
        
    for line in csv_reader:
        print(line['email'])        #Using Dict- for reading only email 
'''

#Dictionary Writer

'''
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open('new_names.csv','w')as new_file:
        fieldnames = ['first_name','last_name','email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter = '\t')
        
        csv_writer.writeheader()
        
        for line in csv_reader:
            csv_writer.writerow(line)
        
'''