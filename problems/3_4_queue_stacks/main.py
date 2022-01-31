'''
Implement a MyQueue class which implements a queue using two stacks

RESOLUTION

The idea here is to emulate a queue with two stacks, for this
we gonna use a Stack A and B
we push data to stack A and once the pop operation
is requered we put all data from A to B, and pop from B until B
is empty
and repeat the operation every time B is empty
'''


class MyQueue:
    def __init__(self) -> None:
        self.A = []
        self.B = []
        self.size = 0
        self.isEmpty = True

    def enqueue(self, data):
        self.size += 1
        self.isEmpty = False
        self.A.append(data)

    def dequeue(self):
        if self.isEmpty:
            Exception("Queue is Empty!")

        # from here I know My stacks are not empty
        if not self.B:
            self.shiftStacks()

        if self.size == 1:
            self.isEmpty = True

        self.size -= 1
        return self.B.pop()

    def shiftStacks(self):
        # while A is no empty, throw every element
        # from A to B

        while self.A:
            self.B.append(self.A.pop())

    def getSize(self):
        return self.size

    def peek(self):
        if self.isEmpty:
            Exception("Queue is Empty!")

        if not self.B:
            self.shiftStacks()

        return self.B[0]

    def state(self):
        print(f'A: {self.A}')
        print(f'B: {self.B}')
        print(f'size: {self.size}')
        print(f'empty: {self.isEmpty}')


if __name__ == '__main__':
    myQ = MyQueue()
    r = [int(data) for data in input().split(' ')]
    myQ.state()

    while r:

        if r[1] == 0:
            print(myQ.dequeue())
        else:
            myQ.enqueue(r[0])
        myQ.state()
        r = [int(data) for data in input().split(' ')]
