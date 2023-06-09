# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
#         visited = set()
#         while head and head not in visited:
#             visited.add(head)
#             head= head.next 
#         return head if head else None
    
        slow = head
        fast = head 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            if fast == slow:
                while head != slow:
                    slow = slow.next 
                    head = head.next
                return slow 
        return None
        