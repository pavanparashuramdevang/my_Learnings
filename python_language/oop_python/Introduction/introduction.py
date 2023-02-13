import math
'''
object oriented programming is a paradigm of programming 
just like C structured programming way where we use functions and program structure to write program

here we use object/class as base while writing program

in python everything is object, i.e lists, int ,string all are objects 

class/objects have two major structural thing you can say blood and bone of objects

1-> data
2-> behaviors


the objects, classes and their interaction is usually modelled in UML , this is a language 


'''

#python class is created using class keyword 

class myFirstClass:
    pass


# you can create objects of class i.e instantiate, by assigning to an varibale and calling class with () paranthesis

a=myFirstClass()

print(type(a)) 


#you can assign attributes to the object using dot notation

# class point():
#     pass

# p1=point()
# p2=point()

# p1.x=3
# p2.x=4.5

# print(f"p1 {p1.x} p2 {p2.x}")



"""
initializing objects

till now you have seen you need to explicitly code everything, assign everything by you only so
in python its very easy to initilialize the objects 

we can use __init__ function to initialize objects 

there is __new__ operator to create objects but we rarely use that because python handles those
on itself


init function take atleas on argument i.e self

self is not a keyword its may be anything but in python community to represent "this object" we use self
to represent "this class" we use cls 


"""

# class point():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

# #which initializes the point objects by taking arguments x,y like below

# p1=point(3,4) #it assigns the 3 and 4 to x,y of p1 object

# print(p1.x,p1.y)



#we can write a complex class consisting of several methods that is usefull in real life like below

class point():
    def __init__(self,x=0,y=0): #x=0 it initializes x=0 if no arguments are provided
        self.move(x,y) #which moves to point x,y or origin if args are not specified

    def move(self,x,y):
        self.x=x
        self.y=y

    
    def reset(self):#please take a look at how a same method is reused which is why we use oop
        
        self.move(0,0)


    def calc_distance(self,other):#we normally use other to specify other object as whole not perticuler data val
        dist=math.sqrt(
            (self.x-other.x)**2 +
            (self.y-other.y)**2
        )

        return dist
    
    def print_point(self):
        print(f"x-> {self.x} y-> {self.y} ")

    


p1=point()          #no args are provided so intializes it to origin 0,0
p2=point(4,5)

p1.print_point()
p2.print_point()

distance=p1.calc_distance(p2)

print(distance)
p1.move(4,5)

print(p1.calc_distance(p2))



    
