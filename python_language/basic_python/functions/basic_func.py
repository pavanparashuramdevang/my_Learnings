'''
function is a named sequence of code that perform certain computation
i.e its a block of code that perform something which can be addressed using name

python several inbuilt functions thats why its used more because there is a function to everything in python

several functions include 
print() 
int() converts anything to int if possible
str()


'''

#defining our own functions we can define using def key word and name and colen at the end 
#we need to indent the code block which is normal to python

#as name tells it prints numbers from 0 to 9 excluding 10
def print_till_ten():
    for i in range(10):
        print(i,end="   ")
    print()

#the above is only defining we need to call this so we call it using its name and () 
#paranthesis are necessary as it states to interpreter these are functions not some variable

print_till_ten()

print(type(print_till_ten))

#once we have defined a function we can use it inside other function

def repeat():
    print_till_ten()
    print_till_ten()

repeat()#calling repeat function

#just like as in c we can provide arguments to function
def arg_func(my_arg):
    print("you have passed argument : ",my_arg)

arg_func("argument")

#the above is a void function as it doesn't return anything 
#there are functions which return something to called function

def add(a,b):
    return a+b

sum=add(4,5)
print(" the sum of 4 and 5 is : ",sum)




