"""
python provides a pickle module to serialize objects 

what is serialization 

to represent data onto file objects you need to convert them into characters or bytes to store 
and transfer 

pickle helps in that, storing of objects in their form
"""
import pickle
import json


data=['abc','def','ghi']

#to store this list you can use a file object and write every element into newline or in csv
#but when you want to retrive you need to know how to access,you may need to write a specific method
#to extract data in  a form tha is usable

#pickle provides two important metods
"""
dump
load

these are common terms in serialization of web objects
"""

with open("pickled_data",'wb') as file:
    pickle.dump(obj=data,file=file)

with open("pickled_data",'rb') as file:
    serialized_obj=pickle.load(file=file)

print(serialized_obj)


"""
pickle module can pickle most of the objects but it may not work on certain objets like
timer objects,web objects etc for that we use other techniques
"""


"""
serializing web objects 
there are several formats/languages avilable to convert an objecect to certain form and transfer them through
the web

like xml,yaml,csv

json by far the most used format for transfer in web as it doesn't have any capability to 
execute a script and though its object notation in name its just data notation

json also provides similer methods like pickle load and dump

you can seralize the objects using __dict__ method
"""

class contact():
    def __init__(self,first,last):
        self.first=first
        self.last=last

    

c=contact("pavan" ,"abc")

print(json.dumps(c.__dict__))


"""
you can write encoder and decoder functions and pass them through hook to 
customize your json load and dumps but its little complicated and needs full understanding
of how json is structured and __dict__ is structured

"""