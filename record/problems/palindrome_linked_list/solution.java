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
    ListNode first;
    boolean ans;
    public boolean isPalindrome(ListNode head) {
        first = head;
        ans = true;
        reachEnd(head);
        return ans;
    }
    
    public void reachEnd(ListNode node){ 
        if(node == null) return;
        reachEnd(node.next);
        ListNode temp = node;
        if(first.val == temp.val) first = first.next;
        else ans = false;
        return;
    }

}