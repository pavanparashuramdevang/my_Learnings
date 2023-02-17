"""
you may have seen **kwargs and *args in most of the python programs 
what are those 

simply put **kwargs means key word arguments you dont need to use kwargs but ** is what makes it possible


we use super() method to pass unknown arguments to parent calss 
every class has object as base class so finaly all the unknown arguments are passed to object class

"""

class contact():#its inherit object bydefault class contact(object):
    all_contacts=list()

    def __init__(self,name="",email="",**kwargs):
        super().__init__(**kwargs)
        self.name=name
        self.email=email
        self.all_contacts.append(self)
    


class address():
    def __init__(self,city="",pin="",**kwargs):
        super().__init__(**kwargs)
        self.city=city
        self.pin=pin

class friend(contact,address):
    def __init__(self,phone="",**kwargs):
        super().__init__(**kwargs)
        self.phone=phone



friend1=friend("987748",name="pavan",email="pavan@gmail.com",city="banglore",pin="767733")

print(friend1.pin,friend1.phone,friend1.name,friend1.email,friend1.city)



"""
till know its well and good but what * and ** actually do  for that you need to understand about 
design pattern,
* and ** are used to unpack a iterable 
* unpacks tuple, list,string and list like iterable
** unpacks dictionary like iterable that has key-value pair


"""

#lets check *args you can give any name but args is what most python dev use so

def print_names(*args):
    print(type(args))
    print(args)

print_names("pavan","abc","def")

#now you may have get that its printing like a tuple 

#we can check that also by printing type

print(*("pavan","abc"))

#what ** do is it unpacks dictionaries 

mydict={"name":"pavan","email":"pavan@gmail.com"}

for key in mydict:
    print(key)

#consider the same function with kwargs

def print_info(*args,**kwargs):
    print(args)
    print(kwargs)


a=print_info('arg1','arg2',key1='val1',key2="val2")

#you can check type but while using you need to be carefull as sometimes if function have an arg name
#as required arg then there is a chance of mis behavng

print("-----------------------------")
def misbehave(name,*args,**kwargs):
    print(name)
    print(args)
    print(kwargs)


b=misbehave(name="pavan",other_name="abc")#i only specified kwargs but it assumes that i have written for
#name so it doesn't provide any error
#it only considers other_name as the only keyword argument

c=misbehave(no_name="kdjfkdjf")
#it provides error as it require one positional argument thats name like this there is some misbehave
#in program if carefully use it , its a good choice
