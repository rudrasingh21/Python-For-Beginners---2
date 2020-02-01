message = "Hello World"

print(message)

print(len(message))

print(message[0])
print(message[1])

#Print Index from beginning - In example it will not include 4th
#Starting Index
print(message[0:4])
print(message[:5])

#Stop Index
print(message[6:])

#Using Methods
print(message.lower())

print(message.upper())

#i.e String Hello apperas only one time
print(message.count("Hello"))

print(message.count("l"))

#To find index
print(message.find("World"))

#To use Replace method
#Use a new variable and assign value , otherwise it will not work

new_message = message.replace("World","Universe")

print(new_message)

#Adding two Strings

greeting = 'Hello'
name     = 'Rudra'

message = greeting + ', ' + name
print(message)

#for complicated strings , we can use it like below
message = '{}, {}.welcome!'.format(greeting, name)

print(message)

# f string
#For python 3.7+

message = f'{greeting},{name}.Welcome!'
print(message)

message = f'{greeting},{name.upper()}.Welcome'
print(message)

# Adding string and number requires type casting

s = "Total States in USA is : "
num = 25

#here s+num will through error because of Type Error

#str(num)

print(s+str(num))