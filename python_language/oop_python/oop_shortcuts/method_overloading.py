'''
mehtod overloading is a tool in oop where in statically typed structural language we need two different
fucntions to handle different arguments like int and string
in statically typed oop langluages we need two methods but 
in python we need only one method 
'''

"""
default arguments are something you provide as default values at the time of passing arguments

"""

def add(a=0,b=0):
    return a+b

#it works regradless of you provide the arguments or not

print(add())


"""
variable argument list 
I already told that unpacking of * and ** ,and how it connects to  tuple and dictionaries 

variable argument list that only
* takes a list of arguments normally represented using *args
** takes a dictionary as argument i.e key value pair **kwargs used to unpack that
"""

def print_names(*names):#it takes all the arguments and creates a list/tuple named names
    print(type(names))
    for name in names:
        print(name)

print_names("pavan","abc","def")

def print_ages(**kwargs):
    print(type(kwargs))
    for name,age in kwargs.items():
        print(name+": "+ str(age))

print_ages(pavan=22,abc=1)#provide kwargs like this only don't provide like dictionary i.e "pavan":22 its wrong

