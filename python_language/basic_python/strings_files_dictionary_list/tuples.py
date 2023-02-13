'''
tuples are similer or you can say same as lists but the tuples are immutable
then why dont we use lists instead of tuples?
bcz sometimes you need that immutabitlity

we can create a tuple just by separating elements with comma 
t= 1,2,3,4   is a tuple 

it is not necessesary but we normally define tuples inside a () paranthesis having comma separated values


'''

t1=1,2,3,4

print(type(t1))
print(t1)


t2=(6,7,8,9)

t3='a', #this is a valid syntax and specify that t3 is not string its a tuple

print(type(t3))



#tuple assignment 
#you may have seen it in dictionaries d.items() 

#you can assign multiple values in a tuple to variable

t=('this','assignment')
s1,s2=t
print(s1,s2)



""""
list comperhension 
one of the most asked questions in python interviews 

why these are needed
sometimes you want to create a new list using data from other list or iterable

"""

t1=[1,2,3,4,6,8]

#if we wanted to create a list consisting of square of all the elements in list how do you do it
#normally we use a for loop

t2=list()

for elem in t1:
    t2.append(elem**2)



print(t2)

#this is ok but not enough pythonic 
#here we use list comperhensions to assign a list by using data from another list

t3= [t1_elem**2 for t1_elem in t1   ]
print(t3)

#it works you may be thinking how its ,is simple
"""
the first thing after [  specifies the elements you may provide multiple elements to create a multidimentional
list (arrray)   the second is for loop which iterates over a list
you can also specify a condition also like only even square or like that
"""

print("printing even square of numbers in t1")
print(t1)

t4=[elem**2 for elem in t1 if elem%2==0]

print(t4)
