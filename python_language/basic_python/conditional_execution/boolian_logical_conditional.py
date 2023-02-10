'''
boolean expressions are expressions that are either true or false

    python provides inbuilt keywords/operator whatever you want to call 
    True and False    these doesn't belongs to str class but to bool class

'''

print(type(True),type(False))

'''
comparision operator

== , != , >, <, <= ,>=  which are the main comparision operator

is ,is not     also comparision operator but I tend to not use them as == and != do the similer thing with much more control

is and is not may confuse 


'''

a=5;
b=5
c=[1,2]
d=[1,2]

print(a is b)
print(id(a),id(b))

print(c is d)
print(id(c) , id(d))#as you can see it provides false as it checks for equality of 
#id of operands if id is same provides out true else provides output false so use == and != for consisensy
#use is and is not only when you know what are you doing


print(c==d)


'''
there are three logical operator

and , not and or

these are simple boolean logical operator similer to && || and ! in c
please note the above && || and ! doen't work in python
please remember not to use && in python

'''


a=True
b=False

print(a and b)
print(a or b)
print(not a)


'''
conditional execution

python doesn't provide switch statement so you only have if , else and elif to work with conditional exectution

for conditional execution you need to terminate the statement using : at the end 
and need to indent the executable block accordingly

'''

if a==True:
    print("a is true")

elif a==False:
    print("a is false")
else:
    print("a is unrecognized")

'''
nested conditional execution

you can nest any times as possible [20 is max ,python imposes 20 as max depth], as todays interpreter are fast and handles most of the requests
you can nest doesn't mean you have to you need to use functions in execution

I recommend at most 3 nested steps 

'''

a=5

if a<10:
    if a>4:
        print(" a is less than 10 and greater than 4")
    else:
        print(" a is less than 4")
elif a==10:
    print("a == 10")

else:
    print(" a greater than 10 ")