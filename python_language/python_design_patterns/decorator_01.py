'''
decorator is just a function which take another function as argument and returns a function without 
altering source code
'''

def decorator_func(exe_func):
    def wrapper_func():
        print("this is wrapper function")#adding additional functionality this also execute
        exe_func()

    return wrapper_func

def display():
    print("display function ran")

decorated_display=decorator_func(display)

#sdecorated_display()

'''
decorating functions  provides way to add additional functionality with out changing source code
'''

'''
the above written is a simple decorator function
but you came here expecting something like

@decorator_something

this is just a python shortcut for something like

decorated_display=decorator_func(display)

here we pass display to decorator_func to add functionality but we just need to write @decorator to specify 

'''

@decorator_func #which is the function you want to pass another display
def another_disp():
    print("this is another display using @decorator")


another_disp()