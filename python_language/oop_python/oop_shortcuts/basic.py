'''
python provides several builtin functions which are essential in day to day activities like 
'''

#len() function which returns a int which counts the number of elements in it

"""
it works depending on data type like for string it count the number of characters 
for list counts the number of elements in the list
"""

a =[1,2,3]
print(len(a))

"""
Reversed() function takes any sequence as argument and returns copy of that in reverse sequence as return 

"""

b=reversed(a)
b=[elem for elem in b]
print(a)#it doesn't change a
print(b)

"""
Enumerate is a function which returns a tuple in which first is index and the later is item
"""

for index,elem in enumerate(a):
    print(index,elem)