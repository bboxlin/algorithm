# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        cur = dummyHead
        val_dict = collections.defaultdict(list)
        for sub_head in lists:
            while sub_head:
                val_dict[sub_head.val].append(sub_head)
                sub_head = sub_head.next
        good_keys = sorted(val_dict.keys())
        for k in good_keys:
            for node in val_dict[k]:
                cur.next = node
                cur = cur.next
        return dummyHead.next
                