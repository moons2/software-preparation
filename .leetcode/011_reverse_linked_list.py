# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        . listen to clearly
        I. clarification questions
        II. speak your logic solution out load
        III. code
        IV. runtime analysis
        V. desk test
        
        left = None
        
        1 <- 2 
l            ^
m                ^
r                ^
        
        middle.next = left
        left = middle
        middle = right
        
        if right:
            right = right.next


        RUNTIME ANALYSIS
            time:   O(n) sendo n o numero de nós da lista
            space:  O(1) independente do numero de nós, precisaremos de 3 variaveis
        """
        if not head:
            return None
        
        left = None
        middle = head
        right = head.next
        
        if not right:
            return head
        
        while middle:
            middle.next = left
            left = middle
            middle = right
            
            if right:
                right = right.next
        
        return left

""" other cool answer
  <- 1 <- 2 <- 3 ->
p              ^
t                 ^
c                 ^


left, middle = None, head
while middle:

"""