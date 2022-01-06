# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recurse(node):
            if not node or not node.next:
                return
            node.val, node.next.val = node.next.val, node.val
            recurse(node.next.next) 
        recurse(head)
        return head