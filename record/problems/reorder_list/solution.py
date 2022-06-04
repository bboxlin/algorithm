# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        cur = slow.next 
        prev = slow.next = None
        while cur:
            nxtnode = cur.next
            cur.next = prev
            prev = cur
            cur = nxtnode
        
        first = head
        second = prev

        while second:
            fnxt = first.next
            snxt = second.next
            
            first.next = second
            second.next = fnxt
            
            first = fnxt
            second = snxt
            
            
            
             
            
            
            