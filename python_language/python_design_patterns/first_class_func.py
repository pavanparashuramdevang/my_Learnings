'''
we should be able to  treat functions like any other object or variable thats called first class functions
and functions can be passed like any other variable
'''

def square(x):
    return x*x

f=square(4)
print(f)

new_func=square

print(new_func(3))


'''passing an function to functions'''

"""
here i take a function as argument and a list 
and loop through them and return the  output list
i.e [1,2,3.4] output [1,4,9,16]
"""

def cube(x):
    return x*x*x


def my_map(func,args_list):
    res=[]
    for elem in args_list:
        res.append(func(elem))

    return res

in_list=[1,2,3,4]

out_list=my_map(square,args_list=in_list)
print(out_list)


