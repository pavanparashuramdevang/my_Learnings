
#simple term a closures is an inner function that remembers  variables in local scope it was created
#even after outer function is finished exectuing

def outer_func(message):
    msg=message
    
    def inner_func():
        print(msg)

    print(id(inner_func))

    return inner_func #it doesn't execute but retuns the function,id precisesly

my_func=outer_func('hi')#as it returned inner_func id my_func is now points to id of inner_func so they are equal

print(id(my_func))

my_func() #executing inner_func

hello_func=outer_func('hello')

hello_func()
