# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        size = 0
        cur = head
        while cur:
            cur = cur.next 
            size += 1
        
        if size == 0:
            return head
      
        
        k = k % size
        if k == 0:
            return head 
        
        poslast = size - k - 1
        cur = head
        while poslast:
            cur = cur.next 
            poslast -= 1
        
        newhead = cur.next 
        cur.next = None 
        
        curhead = newhead
        prev = newhead 
        while curhead:
            prev = curhead
            curhead = curhead.next
        
        prev.next = head 
        return newhead
            
        