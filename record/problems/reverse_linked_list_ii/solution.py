# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyHead = ListNode(val=0, next=head) 
        
        # cur point to node of left
        cur = head 
        leftprev = dummyHead
        for _ in range(left-1):
            leftprev = cur 
            cur = cur.next 
        
        prev=None 
        for _ in range(right-left+1):
            nxtnode = cur.next 
            cur.next = prev 
            prev = cur 
            cur = nxtnode
            
        leftprev.next.next = cur
        leftprev.next = prev
            
        return dummyHead.next
        
        