"""
in this folder i'm going to explain about strings files lists and dictionaries
as I think the chapters are small and only shows the basic working off all the things 
its better to create a simple single folder which explain most of the related functions

strings list and dictionary are the basic datastructures in python

unlike c here string is a built-in datastructure no need of character array 

list are similer to array of c and provides much more sophisticated and i would say easy way of handling arrays

dictionaries are similer to hashmaps if you ever worked in java ,its just a key value pair
where key must be unique 

"""


name=str()  #we can initialize an empty string using str() class

#remember strings are immutable i.e you can't change them once assigned you only can do operation on them
name="pavan"
print(name)

#as it is immutable you can't be able to append on to string 

#name.append(":a") the code is invalid

print(type(name))

#as python is object oriented language we can do several function on these object alled methods
#here also several methods that can be done on a string object

#len function---> len is a general function which provides the length of an object , not specific to string

print(len(name))



#traversing using for we can traverse the string as list of character, thats true for while also
for letter in name:
    print(letter,end=' ')#it prints every letter in name which is p a v a n provide space between as 
                        #prnt function can be altered by providing arguments 

i=0         #in python also string indexing starts from 0
while(i<len(name)):
    print(name[i],end=' ')
    i+=1



#--->slicing

#we can segment a  string called slicing it is done by [beginig_index  :   1+ending_index]
#1+ending as it is exclusive just like range function

print("\n",name[0:3])#prints the first three letters of name

print(name[:3])#prints the first three letter as it assumes the index to be "0" if "left" of colen is not specified

print(name[3:])#it prints name starts from 3rd index to last index it prints element in last index also 

print(name[:])#it prints the whole string its similer as print(name)

#there is a provision of negetive indexing i.e last index can be indicated using -1


#  -5 -4 -3 -2 -1
#   p  a  v  a  n
#   0  1  2  3  4

print(name[:-2])#prints pav as a is -2 and that index is exclusive

print(name[-1:-3])# it doesn't provide proper output as slicing works in one direction from left to right
                #so left of colem must be small index,(counted positive)

print(name[-3:-1])#it works prints va 

#strings are immutable you can't change them
print(name) #name is pavan

#the below statement provides a assignment error
#name[2]='b'


#in operator provides a boolian value if an element present then true else false

print('b' in name)


#string comparison
# == != > < are the comparision operator
#compares string lexicographically

print(name=='pavan')
print(name<'pavan')