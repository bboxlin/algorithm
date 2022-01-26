# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        faster = head
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        
        for _ in range(n):
            faster = faster.next

        while faster:
            faster = faster.next
            slow = slow.next

        slow.next = slow.next.next
 
        return dummy.next