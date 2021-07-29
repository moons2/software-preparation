'''
Describe how you could use a simple array do implement three stacks

RESOLUTION

An array is a static data struct thas stores data consecutively

And a Stack is a data struct based os the LIFO method, Last in First Out
So the item removed from the stack are always the most recent one

As we need to use a single array to implement three stacks, we need
to make sure no one will overide or violate the other's space.
This way we need to insert in a specially position, every 3 positions
to be more precisely

s1  <-  stack 1
s2  <-  stack 2
s3  <-  stack 3

positions:  0   1   2   3   4   5   6
Arr =       [s1 s2  s3  s1  s2  s3  s1]
and so on..
'''
