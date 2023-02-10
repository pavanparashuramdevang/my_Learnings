'''
lists are mutable datastructures similer to that of arrays in c but it can accomodate data of different
types in a single list

we can initialize lise using [] ,or with list() function/class

'''
#using [] creates a empty list
list1=[]

#the list class also creates a empty list
list2=list()

#using this syntax we can assign values to list
list3=[1,2,"dkfdkf",87.09]


#lists are mutable i.e the elements can be changed after initializing
print(list3)
list3[1]=3
print(list3)



#traversing list
#using normal c like for loop


for i in range(len(list3)):
    print(list3[i],end="  ")

#in pythonic way


for elem in list3: #it iterates through each elem in list
    print(elem)


#list operations i.e +,* operaters can be used on the lists
# the + operater concatenates two lists
# the * operator repeats the list n times

list4=[1,2,3]
print(list3+list4) #which creates a new list concatenating both the lists

print(list4*2) #which creates a new list having list4 2 times


"""slicing the lists
just like the strings we can also slice the lists
here we can also assign values to the sliced part of the list 
which is not possible in strings as they are immutable


"""

print(list4[:])

list4[:1]=[5] #which assigns first element to 5, it assigns only iterable so provide value like list tuple etc
print(list4)


"""list methods 
just like string methods there are several of the list methods you can go through

using dir(list) provides the avilable methods on the list

one of the most used list method is append which adds element to end of the list 
which is used in creation list
pop which removes the last element from list
remove which remove the first occurance of element provided

"""

list5=[1,2,3]
list5.append(4)
list5.append(5)

print(list5)

pop_elem=list5.pop()#which doesn't only removes the value which also returns it so we can store it in a variable
print(pop_elem)
print(list5)


list5.append(3)
print(list5)

#now we have two 3 in the list

list5.remove(3) #it removes the first occurance of 3
print(list5)


#another way to remove is del, which is a function 

del(list5[3]) #deletes the element in third index
print(list5)

#del(list5) #deletes the whole list including the list signature

print(list5)    #this produces error as the del function even removes the list5 as whole including signature


#like del we can perform certain functions on the lists like
# len max min sum etc

print(len(list5))
print(max(list5))
print(sum(list5))
print(min(list5))

