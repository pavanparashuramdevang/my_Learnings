'''
sometimes we need to not stop the execution of program because of a wrong input or something of that sort
mostly for input from user and api we use try and except

try --> which tries to execute the block of code if its not possible its handled using except block


'''

inp=input("enter the integer value : ")

#it only executes the try block if you entered the integer value not a string like pa etc
try:
    int_inp=int(inp)
    print(f"you entered {int_inp} belongs to class {type(int_inp)} ")
except:
    print("integer conversion is not possible for given string")



'''
short-circuit evaluation means for example consider a>=4 and (a/b)<5 
from the above equation if we know that first value is false by boolian logic we know that we need not
to evaluate the next expression to know about the final result so the python short ciruit the evaluation
and only evaluate the full expression only when its required 
'''

a=5
b=0
#by using division by 0 we can show which expression gets evaluated

if a>3 and (a/b)==0:#now it provides 0 division error if we made a>6 then prints the output
    
    print('only a>6 is evaluated')
else:
    print("only a>6 is evaluated")