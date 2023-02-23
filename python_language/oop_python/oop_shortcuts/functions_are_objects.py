'''
everything in python is objects including functions 
'''
#we can use functions as attributes

class sample:
    def print(self):
        print("this is class sample")

def fake_sample():
    print("this is not class sample")

a=sample()
a.print()

a.print=fake_sample #don't use paranthesis which calls function and assigns return value

a.print()


"""
callable objects 

we can make any object callable using __call__ method that accepts a required arguments
"""

class Repeater:
    def __init__(self):
        self.count=0

    def __call__(self):
        return "string"
        

print(Repeater()())#first paranthesis initiate the object and the next calls the Repeater   