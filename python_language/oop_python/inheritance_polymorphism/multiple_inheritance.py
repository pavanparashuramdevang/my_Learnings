'''
multiple inheritance, if you ask me, its not a good thing to implement as one class inherits functionality
from multiple classes 

the simplest and most usefull form of multiple inheritance is called "mixin"

what is a mixin,
basically its a super class which is not meant to be exists on its own, but meant to be inherited by some 
other class to provide extra functionality.


'''

class contact():
    all_contacts=list()
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.all_contacts.append(self)



class mail_sender():
    
    def send_mail(self,message):
        print("sending mail to "+ self.email)

    
#this class doesn't do anything but it allows us to create a new class that inherit both and provide
#additional functionality

class emailable_contact(contact,mail_sender):
    pass

e=emailable_contact("pavan","pavan@gmail.com")
e.send_mail("this is my message")


#why multiple inheritance is bad
"""
because it may cause diamond problem

what is diamond problem

consider there are four classes
object
contact and addressholder
friend

contact and address class inherits from object class

friend class inherits both object and addressholder


consider all 4 have __ini__ method
this may lead to parent class set up twice for every object initialization
which is a problem

you can search and find about this its easy and I don't think its really required as I recommend not
to use multiple inheritance as much as possible

"""

