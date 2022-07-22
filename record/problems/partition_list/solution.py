# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        p1 = i = ListNode()
        p2 = j = ListNode()
        while head:
            if head.val < x:
                i.next = head
                i = i.next 
            else:
                j.next = head 
                j = j.next 
            head = head.next 
        j.next = None 
        i.next = p2.next 
        return p1.next
                