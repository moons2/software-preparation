'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry
        c = 0
        result = ListNode()
        ptr = result
        
        while (l1 is not None or l2 is not None):
            
            op1 = 0
            op2 = 0
            
            # checks
            if l1 is not None:
                op1 = l1.val
                l1 = l1.next
            
            if l2 is not None:
                op2 = l2.val
                l2 = l2.next
            
            # soma
            soma = op1 + op2 + c
            c = 0 if soma < 10 else 1
            # c = soma // 10
            
            ptr.next = ListNode(soma if not c else int(str(soma)[-1]))
            #  ptr.next = ListNode(soma if not c else soma % 10)
            ptr = ptr.next
        
        if c:
            ptr.next = ListNode(c)
        
        return result.next

# Others

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry
        c = 0
        ptr = result = ListNode()
        
        while (l1 or l2):
            
            op1 = 0
            op2 = 0
            
            # checks
            if l1:
                op1 = l1.val
                l1 = l1.next
            
            if l2:
                op2 = l2.val
                l2 = l2.next
            
            # soma
            soma = op1 + op2 + c
            c = soma // 10
 
            ptr.next = ListNode(soma if not c else soma % 10)
            ptr = ptr.next
        
        if c:
            ptr.next = ListNode(c)
        
        return result.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0;
        res = n = ListNode(0);
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next;
            if l2:
                carry += l2.val;
                l2 = l2.next;
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val);
        return res.next;