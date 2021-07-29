# Definition for singly-linked list.
# from queue import LifoQueue

# class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #stack1 = LifoQueue()
        #stack2 = LifoQueue()
        carry = 0
        output = []

        while l1 or l2:
            val1 = l1.val | 0
            val2 = l2.val | 0
            res = val1 + val2 + carry
            carry, out = res // 10, out // 10
            output.append(out)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            return output.append(carry)
        return output


'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #stack1 = LifoQueue()
    #stack2 = LifoQueue()
    num1 = num2 = []

    while l1.next:
        num1.append(l1.val)

    while l2.next:
        num2.append(l2.val)


if __name__ == '__main__':
    node = ListNode

    inp = int(input())

    while (inp > -1):
        n = ListNode(inp)
'''
