"""
Given the head of a linked list, 
remove the nth node from the end of the list and return its head

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    	dummy = ListNode(0, head)
        left = dummy
        faster = head
        
        while faster:
            if n != 0:
                n -= 1
            else:
                left = left.next
            faster = faster.next
        
        left.next = left.next.next
        
        return dummy.next