'''
sets are just your mathematical sets which are relpresented using {}

these have all the properties of sets in mathematics as these are unordered and 
store unique values only

to be honest I never used sets that many times I only known the synatax and use case but i just use
list doing some modifications sorry but in data structure solo part i will definitely use it for performance

'''

myset={1,2,3,3}
print(myset) #it doesn't print 3  

#sets can store any hashable items

myset2={1,2,4,5}

newset=myset | myset2  #union using | or
print(newset)

newset=myset & myset2 #intersection using & and
print(newset)

newset=myset - myset2 #therea are other set operations which you can do on this
print(newset)

