"""tuples are immutable list like datastructure or you can say immutable array
how to initialize it 

simple you use () paranthesis but in actuality you don't need any parantesis to initialize any tuple 
you just simply assign a list of values it is assuemed by python as tuple

a=1,2,3,4  it is a tuple
a=(1,2,3,4)
a=1,      its also a tuple the comma is necessary to distinguish it from integer


whats named tuple
as the name suggest its a tuple which having name for each value consider it as a csv or excel
what you have in first row is heading similerly here we have an assigned names which can be used to
call the values insted of using indedxing

namedtuple is not primary datastructure you need to import it from the colections module
"""

from collections import namedtuple


a=1,
print(type(a))

Stock=namedtuple("Stock","name current high low")
"""
don't confuse it takes two arguments first is the identifier name other is space seperated string
which is like headings in excel
"""


stock=Stock('fb',45,47,43)

print(stock.high)