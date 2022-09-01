# src: https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        .   listen to carefully
        I.  clarification questions
        II. speak logic solution out loud
        III.runtime analysis
        IV. code
        V.  table test
        
        head:   [1, 2, 3, 4, 5]   pos = 2
        slow     ^
        fast              ^
        
        '''
        
        if not head:
            return False
        
        slow = head
        fast = slow.next
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False