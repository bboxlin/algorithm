# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 7/2=3
        # 4/2=2
         
        slow = fast = head
        prev = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next 
            fast = fast.next.next 
        
        if prev == slow:
            return None
        else:
            prev.next = prev.next.next 
        return head