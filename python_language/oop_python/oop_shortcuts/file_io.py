'''
only in the begining of larning we use input and output through the console but in most real world 
applications as python is a scripting language we normally work on files as input and output
we never use console for real world usage

'''
"""
python provides a open() function which can be applied on files to create an file object
provides modes such as r,w,a,rb,wb,wb+ you can read their usage and use depending on your specific usage

you can read contents usign
read()   you can read whole file which is not quite recomonded or you can read fixed bytes by passing an 
            integer as argument

readline() which reads a line which is recomonded ,use it using for loop

readlines() it returns list of all lines so don't use it instead use readline in for loop

"""

content="this is the content to file\n this is new line "

file=open("example.txt",'w')
file.write(content)
file.close()#which is essential

file=open('example.txt','r')
print(file.read())#it works but it is not recomonded as for larger files there may lead to memory overload
#resulting in some unwanted behaviour

file.close()

"""
to overcome any errors etc we use context manager 
context managers are objects with special methods __enter__ and __exit__

"""

print("using context manager ****************")
with open('example.txt') as file:
    for line in file:
        print(line)
