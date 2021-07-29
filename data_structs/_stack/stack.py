'''
Stack, a data struct that stores items in a last-In/First-Out (LIFO) manner.

insertion (push): O(1)
deletion (pop):   O(1)
size:             O(1)
isEmpty:           O(1)

in python, an easy manner to implement a stack is through the
list lib or deque lib, list places each item in a consecutive
memory position, what can become a problem when each item 
has a significant size.

deque on the other hand, is built upon double liked list.
what makes append and pop operations constant time.

STACK AND THREAD

NEVER use list for any data struct that  can be accessed by
multiple threads. list is not thread safe

deque, however are specially thread safe for the .append()
and .pop() method, once they are supposed to be atomics.

if you want to built a fully stack thread safe, you should use
the LifoQueue from deque, i.e

from queue import LifoQueue, this is fully thread safe

Stack are usefull in certain kind of recursive algorithms.
Sometimes you need to push an item at a stack while you
recurse but them removing them backtracking.

bibliograpy:
https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html
https://realpython.com/how-to-implement-python-stack/

LET'S CODE

The implementation of choice for an abstract data type is the 
creation of a new class. The operations are implemented as methods

'''

from os import error
from queue import LifoQueue


class Stack:
    def __init__(self):
        self.stack = LifoQueue()
        self.size = 0

    def push(self, item):
        self.size += 1
        self.stack.put_nowait(item)

    def pop(self):
        self.size -= 1
        return self.stack.get_nowait()

    def isEmpty(self):
        return self.stack.empty()

    def getSize(self):
        return self.size

    def getNativeSize(self):
        return self.stack.qsize()
