/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA;
        ListNode b = headB;
        while(a != b){
            //Alist走完到Blist， Blist走完到Alist 最早碰到的一个就是交叉node
            a = (a!=null) ? a.next:headB;
            b = (b!=null) ? b.next:headA;
        }
        return a;
    }
}