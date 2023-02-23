'''
lists are like goto structures in python if you don't know what you are doing exactly just use lists
lists are multipurpose and can be used in multiple ways like with little modification it can be turned into
stack 

lists are defined using [] square brackets and list() class
one of the importent method in lists are append() which adds values to end of the lists which is 
used very often while doing anything related to not only list but to python itself

some of the important methods are explained below with structure of arguments
'''

mylist=list()

for i in range(10):
    mylist.append(i) #append takes one arg which is element to be added at the end of the list

print(mylist)

#insert(index,element)

mylist.insert(5,3)
print(mylist)

#count(element) tells us how many times element in list
print(mylist.count(3))

#index(element) it returns first index and if not then valueError so use carefully

print(mylist.index(3))

#find(element) similer to index method but instead of ValueError it returns -1

#print(mylist.find(23)) i don't know why but there is no find method 

#reverse() as the name suggest it reverses the list it perform inplace reverse so it reverses the list
#itself,it doesn't provide a copy of the reversed list, it reverses the list itself

mylist.reverse()
print(mylist)

#sort() this is also inplace sort

mylist.sort()
print(mylist)
