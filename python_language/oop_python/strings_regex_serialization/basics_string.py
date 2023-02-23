"""
you may be thinking we know all about strings 
but na,strings are the most complicated as there are different encodings and
different way of representing strings,formatting strings

"""

for methods in dir(str):
    print(methods)


"""
you can see different methods for string manipulation
methods like count,find ,index are already explained

but in real world we need to split the string based on certain characters like , for csv @for email etc

and another important thing is removing the white space at the begining and at the end

joining strings by certain character 
"""

s=" hello how are you  "

s=s.strip(' ')

s2=s.split(' ')#it splits based on space ' '

print(s2) #converts it into a list

#we can join using a string
s3="@".join(s2)
print(s3)

#we don't want starting and ending spaces normally it is quite common to remove we use a method
#called strip(), rstrip(),lstrip() normally strip() is used 

"""
in olden days people are using string.format(args) to format strings but
I normally use f"" strings where we directly embed the arguments inside the stirng so 
it looks clear and more readable
"""

a="first arg"
b="second arg"

print(f"this is formating using f strings {a} and {b}")

#the same can be printed using
template="this is formating using not f strings {} and {}" #you don't need to write in separate string

print(template.format(a,b))

#theres a question what if we wanted to print braces 

print(f"this is formating using f strings {{a}} and {{b}}")


"""
just like args you can also pass kwargs 
"""

template="""
from = {from_email}
to :{to_email}
sub:{subject}
"""

print(template.format(
    from_email="pavan@gmail.com",
    subject="this is the subject",
    to_email="abc@gmail.com"
))


"""
container lookup till now we sent args kwagrs but what if we sent a tuple,list or a dictionary
we can do that and also 
"""

email=("pavan@gmail.com","abc@gmail.com")
message={
    'subject':"this is the subject"
}

template="""
from = {0[0]}
to :{0[1]}
sub:{1[subject]}
"""
print(template.format(
    email,message
))


"""
how to look in an object then 
"""
class test():
    def __init__(self,name,usn):
        self.name=name
        self.usn=usn

a=test("pavan","123")
b=test("abc","234")

template="""this is formatted using objects
name1 : {0.name}  name2 : {1.name}
usn1 : {0.usn}  usn2 :{1.usn}
"""

print(template.format(a,b))

#just use fstring it is more readable
print(f"printed using fstring and objects name1 ={a.name} name2 ={b.name} usn1={a.usn} usn2={b.usn}")

