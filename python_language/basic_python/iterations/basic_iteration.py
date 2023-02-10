'''
basically python provides two types of loops to iterate over a set of values 
while and for
while is similer to that of C while loop
but for is littele different ,you learn that in iterator pattern in design  pattern
'''

x=1#initializing a variable/counter 
while(x<5):
    print(x)
    x+=1#don't use x++ as it is not supported for a very good reason (x++ ++x its confusing)
    
#infinite loops using while 

#infinite doesn't it always run, here we break out of the condition using break statement
#rather initially explicitly stating the condition 
i=0
while True: #it results in infinite loop
    if(i<5):
        print(i)
        i+=1
    else:
        break #explicitly exiting out of loop using break

#continue is similer to that of c continue where it resets the control flow to beginig of loop 
#without running the code below it


#printing even number using continue
i=0
print("\n printing even numbers less than 10")
while(i<10):
    if(i%2 == 1):
        i+=1
        continue
    else:
        print(i)
        i+=1


'''
we call for loops as definite loops in python as it is used to iterate over a definite set of things 
like a list of number ,
items in a dictionary ,set
or evern on any iteratable object i.e soup object from website html(beautifulsoup)

'''

friends=['abc','def','ghi','jkl']

#we need to iterate over all the elements in friends in c we normally do in this way
#c way
i=0
print("iterating over a list in c way")
for i in range(len(friends)):
    print(friends[i])


#it works but its not the pythonic way, we use iterator pattern while using for loop 
print("\n iterating in pythonic way")
for friend in friends:          #friend variable is a placeholder, we may write any thing ex i,j
                                #friend variable stores friends[i] at a perticuler point in iteration
    print(friend)
