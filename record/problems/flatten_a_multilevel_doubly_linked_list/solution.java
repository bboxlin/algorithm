/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        
//         if(head == null) return head;
//         Stack<Node> stack = new Stack<>();
//         Node cur = head;
//         while(cur!=null){
//             if(cur.child != null){
//                 if(cur.next != null){
//                     stack.push(cur.next); //储存先级头
//                 }
                
//                 cur.next = cur.child; //连接二级值
//                 cur.next.prev = cur;
//                 cur.child = null;
//             }else if(cur.next == null && ! stack.isEmpty()){ //到尾巴了
//                 cur.next = stack.pop();  //连接储存的先级头
//                 cur.next.prev = cur;
//             }
            
//             cur = cur.next;
//         }
//         return head;
        
        if(head == null) 
            return head;
        Node curr = head;
        Stack<Node> stack = new Stack<>();
        
        while(curr != null){
            if(curr.next != null) stack.push(curr.next);
            if(curr.child != null) stack.push(curr.child);
             
            if(stack.isEmpty()) break;
            curr.child = null;
            curr.next = stack.pop();    
            curr.next.prev = curr;
            curr = curr.next;
        }
        return head;
    }
}