# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        while head:
            nextnode = head.next 
            head.next = prevNode
            prevNode = head
            head = nextnode
        return prevNode
             