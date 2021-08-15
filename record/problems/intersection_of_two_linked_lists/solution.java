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
//         ListNode cur = headA;
//         int lenA = 0;
//         while(cur != null){
//             lenA ++;
//             cur = cur.next;
//         }

//         cur = headB;
//         int lenB = 0;
//         while(cur != null){
//             lenB ++;
//             cur = cur.next;
//         }
//         ListNode curA = headA;
//         ListNode curB = headB;
//         if(lenA > lenB) {
//             for(int i=0; i<lenA-lenB; i++){
//                 curA = curA.next;
//             }
//         }
//         if(lenA < lenB)  {
//             for(int i=0; i<lenB-lenA; i++){
//                 curB = curB.next;
//             }
//         }
//         while(curA!=null){
//             if(curA == curB) return curA;
//             curA = curA.next;
//             curB = curB.next;
//         }
//         return null;
        
        
        
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