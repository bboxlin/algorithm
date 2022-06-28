# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prevHead = ListNode(0)
        node, node1, node2 = prevHead, l1, l2
        while node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next 
            else:
                node.next = node2
                node2 = node2.next 
            node = node.next
        if node1:
            node.next = node1 
        if node2:
            node.next = node2 
        return prevHead.next
            