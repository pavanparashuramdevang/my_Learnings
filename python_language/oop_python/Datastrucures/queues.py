'''
in lists we can insert and remove elements from any index but normally we want to limit this 
so we use queues 
fifo queues
lifo queues also called stacks


'''

"""
fifo queues there are some methods on it which are very helpfull like
put(),get(),full(),empty()


"""

from queue import Queue
from queue import LifoQueue
line=Queue(maxsize=3)

line.put(1)
line.put(2)
line.put(3)
#line.put(4)#it waits infinitely as the queue is full to mitigate this we use timeout
#line.put(4,timeout=1)#which runs and exits with exception queue.Full

print(line.get(block=False))
print(line.get(block=False))
print(line.get(block=False))
#if block=False is not provided then it also waits for infinitely
# print(line.get())

'''
lifo queues or stacks
these also provdes same functionality like get put and empty etc
'''

stack=LifoQueue(maxsize=3)
stack.put(1)
stack.put(2)
stack.put(3)
# stack.put(4)#same it also waits infinitely
# stack.put(4,timeout=1

print(stack.get(block=False))
print(stack.get(block=False))
print(stack.get(block=False))
#print(stack.get())
