'''
as string is a object we can perform certain functions on them called methods
we can find out the avilable methods on any object using

dir(object_name) or dir(sample_object)


'''
print(dir(str))#prints the methods on string

name='pavan'
new_name=name.capitalize()#you have to use ()paranthesis or else it assigns the address to variable
print(new_name)

#upper convert to uppercase ,lower converts to lower case
print(name.upper(),name.lower())

#find method finds the presence of letter/element and returns the index
index=name.find('va')#finds the first accurance of element if not present returns -1
print(index)

#there are several methods like 
'''
strip removes the whitespaces in begining and end
rstrip to remove the right side whitespaces
lstrip to remove the left side whitespaces

'''

word='    without whitespace   '
print(word.strip(),"|",word.lstrip(),"|",word.rstrip(),"|")

#parsing a string

url='From stephan.marq@uct.ac.za sat jan '

#if we wanted to find uct.ac.za we can do that 

at_position=url.find('@')

#to find the space after @ we need to specify @ index to find method
space_position=url.find(' ',at_position)#it serches for space from at positon

host=url[at_position+1 : space_position]
print(host)


"""
format operator

it acts similer to that of c percent operator in printf scanf statements

% replaces the position with a data stored in variable

"""

camel=45.3

print("the camel value is %.2f "%camel)#don't use comma , between the percent symbol it produces the error
#as you can see its formatting also works similer to that of c 

