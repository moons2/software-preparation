# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        .   listen to clearly
        I.  clarification questions
        II. speak your solution logic out load
        III. code
        IV. runtime analysis
        V.  table test

        Q1. Posso retornar uma nova lista como resultado ou deve ser in-place?
        Q2. pode ocorrer de uma das listas ser nula
        Q3. Em caso de nula o que devo retornar?

        1 -> 2 -> 3
                     ^

        0 -> 2 -> 4 -> 4
                       ^

        0 -> 1 -> 2 -> 2-> 3 -> 4 -> 4
        ^

        analise de complexidade
        tempo:  O(m + n), sendo m o numero de nós na lista 1, e n o numero de nós na lista 2
        spacial: O(m + n) sendo m o numero de nós na lista 1, e n o numero de nós na lista 2
        """
        runner1 = list1
        runner2 = list2
        output  = ListNode()
        runnerOutput = output

        while runner1 or runner2:
            if runner1:
                if runner2:
                    if runner1.val < runner2.val:
                        runnerOutput.next = ListNode(runner1.val, None)
                        runner1 = runner1.next
                    else:
                        runnerOutput.next = ListNode(runner2.val, None)
                        runner2 = runner2.next
                else:
                    runnerOutput.next = ListNode(runner1.val, None)
                    runner1 = runner1.next

            elif runner2:
                if runner1:
                    if runner1.val < runner2.val:
                        runnerOutput.next = ListNode(runner1.val, None)
                        runner1 = runner1.next
                    else:
                        runnerOutput.next = ListNode(runner2.val, None)
                        runner2 = runner2.next
                else:
                    runnerOutput.next = ListNode(runner2.val, None)
                    runner2 = runner2.next
                    
            runnerOutput = runnerOutput.next
        
        return output.next

