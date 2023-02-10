"""
the python provides operators like + - * / ** %

+ for addition
- for subtraction
* for multiplication
/ division in python 3 it is floating point devision 
// for integer division
** exponent i.e power
% modulus operator



"""

a=5
b=2

print(a+b," ",a-b," ",a*b," ",a/b," ",a//b," ",a**b," ",a%b)

"""
input is a very simple topic in python
as input function handles most of the string input from the console and translates it into string 
"""
string="enter your input : "
inp=input(string)

print(type(inp))
#you can see type of inp is string and input function considers everything to be string
#we need to typecast input into usable form

print("you entered : "+inp)

num1=input("enter first number : ")
num2=input("enter the second number : ")

print(num1+num2)#you can see it concatanates the two numbers like operation on cls str

print(int(num1)+int(num2))

