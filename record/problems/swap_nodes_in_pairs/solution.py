# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        # if not head or not head.next:
        #     return head 
        # firstnode = head 
        # secondnode = head.next 
        # firstnode.next = self.swapPairs(head.next.next)
        # secondnode.next = firstnode 
        # return secondnode
        
        dummyhead = ListNode(next=head)
        prev, cur = dummyhead, head
        while cur and cur.next:
            first = cur 
            second = cur.next 
            
            prev.next = second
            first.next = second.next
            second.next = first 

            cur = first.next 
            prev = first 
            
        return dummyhead.next
            
        
        
        
    
    
    
        