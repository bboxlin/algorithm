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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode sum = head;
        int cin = 0;
        while(l1 != null  || l2 != null){
            int l1_val = (l1 == null) ? 0 : l1.val;
            int l2_val = (l2 == null) ? 0 : l2.val;
            
            int cur_sum = l1_val + l2_val + cin;
            cin = cur_sum / 10;
            int last_digit = cur_sum % 10;
            
            ListNode new_node = new ListNode(last_digit);
            sum.next = new_node;
            
            if(l1 != null) l1=l1.next;
            if(l2 != null) l2=l2.next;
            sum = sum.next;
        } 
        if(cin>0){
            ListNode new_node = new ListNode(cin);
            sum.next = new_node;
        }
        return head.next;
         
    }
}