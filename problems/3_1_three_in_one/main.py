'''
Describe how you could use a simple array do implement three stacks

RESOLUTION

An array is a static data struct thas stores data consecutively

And a Stack is a data struct based os the LIFO method, Last in First Out
So the item removed from the stack are always the most recent one

As we need to use a single array to implement three stacks, we need
<<<<<<< HEAD
to make sure no one will overide or violate the others' space.
=======
to make sure no one will overide or violate the other's space.
>>>>>>> fce927b8a437975244a9e2a523fbc7aaea04f8a7
This way we need to insert in a specially position, every 3 positions
to be more precisely

s1  <-  stack 1
s2  <-  stack 2
s3  <-  stack 3

positions:  0   1   2   3   4   5   6
Arr =       [s1 s2  s3  s1  s2  s3  s1]
and so on..
<<<<<<< HEAD

but this manner will be a little difficult

'''


class Stack3in1:
    '''
    the strategy here is to make three stacks
    '''

    def __init__(self):
        self.stacks = [[], [], []]
        self.emptys = [True, True, True]
        self.peaks = [None, None, None]
        self.sizes = [0, 0, 0]

    def push(self, data, stack_no):
        if not (0 < stack_no < 4):
            Exception("Stack index out of range!")

        self.stacks[stack_no-1].append(data)
        self.peaks[stack_no-1] = data
        self.sizes[stack_no-1] = len(self.stacks[stack_no-1])

        self.emptys[stack_no-1] = False

    def pop(self, stack_no):
        if not (0 < stack_no < 4):
            Exception("Stack index out of range!")

        if self.emptys[stack_no-1]:
            return

        if self.sizes[stack_no-1] == 1:
            self.emptys[stack_no-1] = True
            self.peaks[stack_no-1] = None

        poped = self.stacks[stack_no-1].pop()
        self.sizes[stack_no-1] -= 1
        self.peaks[stack_no-1] = self.stacks[stack_no-1][-1]
        return poped

    def peak(self, stack_no):
        return self.peaks[stack_no-1]

    def isEmpty(self, stack_no):
        return self.emptys[stack_no-1]

    def getSize(self, stack_no):
        return self.sizes[stack_no-1]

    def stacksState(self):
        print(self.emptys)
        print(self.peaks)
        print(self.sizes)


if __name__ == '__main__':
    myStack = Stack3in1()

    myStack.stacksState()

    reads = [int(data) for data in input().split(' ')]

    while reads[1] > 0:
        myStack.push(reads[0], reads[1])
        myStack.stacksState()
        reads = [int(data) for data in input().split(' ')]
=======
'''
>>>>>>> fce927b8a437975244a9e2a523fbc7aaea04f8a7
