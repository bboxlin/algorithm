/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // ListNode prev = null;
        // ListNode cur = head;
        // ListNode next = null;
        // while(cur!=null){
        //     next = cur.next; //next value stored 
        //     cur.next = prev; //a pointer reverse
        //     prev = cur;   // prev updated to next node
        //     cur = next;   // cur updated to next node 
        // }
        // return prev;
        
        
    if (head == null || head.next == null) return head;
        ListNode next = head.next;
        head.next = null;
        ListNode p = reverseList(next);
        next.next = head;
        return p;
    }
}