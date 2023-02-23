"""
dictionaries are like key value pairs

for dictionaries you need to understand is idioms,in python you get several code structures
which are used most of the time and which are recomonded as it increases readability and extensibility

as it is said code is written once and read thousand times
best practises make your code cleaner and appriciated

here key and values are seperated using Colen : so don't use = as it is for assignment
most of the time  i write using equals and then fix it so please check twice while using dictionaries

thes are represented by {} and these are unordered

"""

stocks={'goog':(54,56,52),
        'msft':(112,132,98)
        }

print(stocks['goog'])#you access values using keys

"""
accessing like this is not good because it may results in keyerror  so to eleminate this and for other
reasons we normally use get method to access values 

get method accepts two arguments keyvalue and default value
if key found in dict then return dict[key] else returns default value

"""
#print(stocks['apl']) #produces KeyError

print(stocks.get('apl','not found'))

"""
we are only getting default values are return we are not doing anything with that values
like set it, like if new stock comes we need to set it to 0 or something like that

we use setdefault method which is similer to get
but it also set the values into dictionaries
"""

print(stocks.setdefault('apl',(0,0,0)))

print(stocks)

"""
we can't setdefault on existing values obviously
we can't set the values of goog to 0,0,0 as it is already set

"""

print(stocks.setdefault('goog',(0,0,0)))
print(stocks)

"""
there are three main other methods 
keys(),values(),items()

as the name suggests it returns keys, values and (key,value) tuples respectively
"""

for key,value in stocks.items():
    print(key,value)


"""
one of the best uses of dictionaries for demonstration is letter frequency 
"""

def letter_frequency(sentence):
    frequency={}
    for letter in sentence:
        frequency.setdefault(letter,0)
        frequency[letter]+=1
    return frequency

print(letter_frequency("ababaa"))

"""
other then this there are several methods like defaultdict,counter which are in collections module
"""

