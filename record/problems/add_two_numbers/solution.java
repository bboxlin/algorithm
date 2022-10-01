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
        ListNode dummyHead = new ListNode();
        ListNode curnode = dummyHead;
        int carry = 0;
        while (l1 != null || l2 != null || carry>0){
            int cursum = 0;
            if (l1 != null){
                cursum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                cursum += l2.val;
                l2 = l2.next;
            }
            
            cursum += carry;
            
            if (cursum >= 10){
                carry = 1;
            }else{
                carry = 0;
            }
            
            ListNode newNode = new ListNode(cursum % 10);
            curnode.next = newNode;
            curnode = curnode.next;
        }
   
        
        return dummyHead.next;
    }
}