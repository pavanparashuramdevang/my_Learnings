"""
you may have seen some error messages poped out while executing something

you can define your own errors and error messages called raising exception

you can use raise keyword to raise exception


"""


def div(num1:int,num2:int)->int:
    if num2==0:
        raise ZeroDivisionError("can't be devided by zero")
    else:
        return num1/num2
    
print(div(3,4))

#in the abouve you know zerodivisionError occures and already an exception defined for that so you
#use that to raise perticuler error

"""
what to do when you can't find a error type defined for your perticuler case 

then you normally use and Exception along with a message that explains that error

"""

def no_return():
    print("this will be printed")
    raise Exception("this is error message raised")
    print("this will not be printed")
    return("no return")




"""
now we are raising exceptions but we don't want to stop our program execution
we can handle exception using 

try and except block


"""

try:
    no_return()

except:#it doesn't halt the program 
    print("caught an exception")


"""
its not a good idea to handle every exception with one except call

we need to be precise about errors so we handle every error differntly


"""

try:
    no_return()

except ValueError:
    print("value error excetption handled")

except TypeError:
    print("type error excepton is handled")

except Exception:
    print("exception is handled")

#we can be precise on handling 


"""
try and except is not enough for good programming

we use else to indicate that program executed without error i.e else executes if no error occures

we use finally to do some cleanup after the execution is complete

"""

try:
    #no_return()
    print("")
except:
    print("some exception occured")
else:
    print("no exception occured program run safely")

finally:
    print("clean up code ")