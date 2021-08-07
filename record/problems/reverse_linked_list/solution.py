# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead = None
            
        while head:
            nextNode = head.next
            head.next = newhead
            newhead = head
            head = nextNode
        
        return newhead