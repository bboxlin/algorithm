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
    public ListNode partition(ListNode head, int x) {
        
        ListNode l1 = new ListNode(0);
        ListNode l2 = new ListNode(0);
        ListNode head1 = l1;
        ListNode head2 = l2;
 
        
        while(head!=null){
            if (head.val<x){
                l1.next = head;
                l1 = l1.next;
            }else{
                l2.next = head;
                l2 = l2.next;
            }
            head = head.next;
        }
        l2.next = null;
        l1.next = head2.next;
        return head1.next;      
    }
}