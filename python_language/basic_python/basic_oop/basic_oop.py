'''
I have skipped several chapters from the book like regex, networking ,json
I think you can  go through them easily as they are industry specific you need learn them 
I may talk about that if I got time or else those are just basics anyway 

the concepts are way deep to understand like regex I can only show you about how to create how to use
but the concept of regex is very big and in my CS course its a whole module,its a language by itself
so learn what is required for working with python

'''

"""
object oriented programming

now a days every enterprise software or any software is written in oop only 
the languages like c++ ,java,c#,kotlin,js,Ts 
every vendor who provides a language says it supports every paradigm but all are used to write oop
code at the end of the day 

why oop?
simple because of reusabiliy,security(access modification) 


there are four pillers in oop

Abstraction
Encapsulation
polymorphism
Inheritence


"""

"""
in python everything is an object

there are two important concept in oop 
the object
the class

class is a framework of how an object should be 
object is a real world instance that belongs to certain class


"""

#we can define a class using class keyword

class Party_animal:
    x=0

    def party(self):
        self.x=self.x+1
        print("so far",self.x)

animal=Party_animal()  #creating an instence of class party_animal, () are necessary though you are not specified in creaion of class
animal2=Party_animal()
animal.party()
animal.party()

#you can create a new animal and it works as its totally differnt object like two seperate persons
animal2.party()



#python __new__ and __init__ methods


#if you have work with jave you have seen new keyword which is used to create object 
"""
in python we rarely use the __new__ method to create an object but python do it for us internally
we normally use __init__ to create and initialize the object at the same time


point and rect is the basic objects that shows the potential of oop 

we use self in python to specify this, you may have used this in java
self is not a keyword but its a standard followed by python community
self says that use this object

"""

class point():
    def __init__(self,x=0,y=0):#it initializes the point with given x and  y cordinate if none is given then initializes x=0 y=0
        self.x=x
        self.y=y

    def print_point(self):
        print(f"x-->{self.x} y-->{self.y}")

    
p1=point()

p1.print_point()


"""
Inheritence one of the four pillers of the oop

its when a child inherit the methods and variables of the parent class

consider a scenaria, vehicle -->  {car,van,bus}

car is a child and vehicle is parent 

we can model the same using oop
"""

class vehicle():
    def vehicle_method():
        print("this is written in vehicle class")


class car(vehicle):  #argument passed is the name of the parent you can pass multiple names, resulting in multiple inheritence
    def __init__(self,company,year):
        self.company=company
        self.year=year

    def print_car(self):
        print(f"the car company is {self.company}\nthe car manufactured in year {self.year}")


car1=car('Tata','2020')

car1.print_car()

'''
we have not initialized the vehicle class but we are capable of executing its methods 
from the car class as car inherit the vehicle


'''

car.vehicle_method() 
