'''
dictionaries are key-value pair and they are like hashmaps of java
and look similer to json objects in structure so we can convert dict to json and vice-versa
using json library and load and dump functions

dictionaries do not indexes the elements based on position so you have to retrive item using key

you can create a dictionary by invoking dict() class
and like [] for list python provides {} to initialize the dictionaries 
key and valuse should be seperated by : colen 

else if there is no colen then it is considered as set
'''

students={1:'pavan',2:'abc',3:"def"}

print(students)

#to access an element we need to use key to specify the item
print(students[2])  #the two here is not the index, dict doesn't indexes based on pos


#if no key found results in keyError


"""
dictionary as a set of counter i.e character counter

there is a idom in python to use dictionary as a counter

"""

word="pavan"

word_count=dict()

for character in word:
    if character not in word_count:
        word_count[character]=1   #initializing character count to 1

    else:
        word_count[character]+=1 #incrementing character count

print(word_count)



"""
there is another way of achiving the same in less lines and more of a pythonic way
you have to remember it most used for showing off your skill in python
"""

d=dict()

for c in word:
    d[c]=d.get(c,0)+1  #this is idiom where get is used it assigns 0 initially for non occured items


print(d)


#looping through the dictionaries

for key in word_count.keys():     #it only iterates through set of keys
    print(key)

#printing only values 
for values in word_count.values():
    print(values)


#for iterating over both keys and values

for key,value in word_count.items():  #which returns a tuple consisting of key and value
    print(key," : ",value)

