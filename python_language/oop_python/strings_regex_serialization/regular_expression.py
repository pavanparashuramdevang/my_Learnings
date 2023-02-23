'''
regular expressions are very much required for any type of software related work
it may be frontend,fullstack you must have the understanding of regex 

regular expressions are a language by itsef ,if you are cs background then it is taught in automata theory
this is a minimal language which is used to manipulate the strings down to single characters

grep is a popular tool in linux community which is an example of regex usecase
grep stands for global regular expression print 
you can say grep is a wrapper for regular expression 

what we can do with regex

normally we search for patterns in a string using some kind of language 
that consists of characters,special characters,escape characters etc

re is python regular expression module
'''

import re

search_string="this is the string you search for hello "

pattern=r".*hello.*"  #we normally provides raw string for pattern as it consists of several regex specific 
    #symbols and characters otherwise we may need to escape them using \ backslash
    #.* means match anything any number of time
match=re.match(pattern=pattern,string=search_string)

if match:
    print("regex matches")
else:
    print("not match")


"""
there is a list of how to represent pattern to search for certain thing in regex 
which differ slightly from one language to other 
python regex is different from grep but underlying concept remains the same
"""

"""
meta characters                 uses

.     (period)                 -matches any characters except the newline
\d                             -degit (0-9)
\D                             -not a degit opposite of \d
\w                             -word character(a-z,A-Z,0-9,_) it also matches underscore
\W                             -not word character i.e opposite of \w
\s                             -whitespace (space,tab,newline)
\S                             -not whitespace
\b                             -word boundary i.e start of word
\B                             -opposite of \b

^                              -begining of the string
$                              -end of the string



quantifiers

*       -matches 0 or more characters
+       -matches 1 or more characters
?       -0 or 1 character
{3}     -exact number
{3,4}   -range of numbers ( minimum,maximum)

*************************************
[]      -specifies the character set and matches only one character from the set
|       -either or 
()      -group
"""

phno="""
123-123-1233
123,134,1543
1234-123-874 not a phone number
"""

pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern2=re.compile(r"\d{3}.\d{3}.\d{4}")

match_iter=re.finditer(pattern=pattern2,string=phno)

for match in match_iter:
    a,b=match.span()
    
    print(phno[a:b])


"""
there are other method like findall match etc which are usefull sometime but I prefer finditer as
it provides a iterable and its easy to work with
"""