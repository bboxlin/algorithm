# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        cur = dummyHead
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                prevval = cur.next.val 
                while cur.next and cur.next.val == prevval:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyHead.next
            
                
            
            
            
            