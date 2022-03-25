# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq = {}
        cur = head
        while cur:
            freq[cur.val] = 1 if cur.val not in freq else freq[cur.val] + 1
            cur = cur.next
        
        dummyHead = ListNode(next=head)
        cur = dummyHead
        while cur and cur.next:
            if freq[cur.next.val] > 1:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyHead.next