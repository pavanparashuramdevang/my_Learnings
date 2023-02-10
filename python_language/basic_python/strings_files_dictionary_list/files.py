'''
there are two kinds of files 
text files and binary files 

in python we mostly work on text files

python provides a function  called "open" to work with files
if file doesn't present open function creates the file and opens it

to close the file we use close function 

in python we normally use context manager to open a file and manage it for us 
     with open : is a context manager
which is what manages and closes the file after working with it automatically

'''

# file=open("file1.txt","w")

# #to write to function

# for i in range(10):
#     file.write(str(i))      #it writes only string object to file

# #you need to close the file to read it again
# file.close()

file=open("file1.txt","r")

"""
reading and writing to file is little bit complicated as at first you think of reading an entire file 
which works but when you don't know the size of files which may be of GB in size which we don't want

we try to read files in chunks rather as whole

"""

#reading file as whole
print(file.read())


for line in file:
    print(line)
    print("*****")

#we use with open  because the file pointer is already in end after file.read() operation
#to minimize the errors like this we use with open context manager

with open('file1.txt') as f:
    for line in f:
        print(line)
        print("######")

