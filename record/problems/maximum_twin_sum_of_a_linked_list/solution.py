# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head,head 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 
        
        # reverse second part list
        prev, cur = None, slow 
        while cur:
            nxtnode = cur.next 
            cur.next = prev
            prev = cur 
            cur = nxtnode 
        
        # one point first part, the other point second part
        first = head 
        second = prev 
        
        ans = 0
        while second:
            ans = max(ans, first.val + second.val)
            first = first.next 
            second = second.next 
        
        return ans 
            
        
        
        