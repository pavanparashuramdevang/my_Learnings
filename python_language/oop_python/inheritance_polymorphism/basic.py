'''
python as this overlapping non oops way of approching object oriented program

basic inheritance is simply inheriting values and methods from the parent class

consider a class parent  and a class child

'''

class parent():
    parent_val="this is parent non init value"

    def __init__(self):
        self.val="this is parent init value"

    def move(self):
        print("parent moving")


class child(parent): #you need to provide the class name inside the paranthesis to make inheritance

    def __init__(self,name):
        self.name=name


child1=child('pavan') #only child is initialized with not the parent i.e you can't access parents val variable

print(child1.parent_val)

child1.move()
print(child1.val)#value is not initialized as its only refering to parent, that is not initilized


# par1=parent()

# print(par1.val) #this works because its initialized not inherited


    