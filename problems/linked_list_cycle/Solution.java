/**
 * https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
 * 
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    public boolean hasCycle(ListNode head) {
        
        if(head == null)
            return false;
        
        ListNode slow = head;
        ListNode fast = slow.next;
        
        while (fast != null && fast.next != null)
        {
            if(slow.equals(fast))
                return true;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return false;
    }
}