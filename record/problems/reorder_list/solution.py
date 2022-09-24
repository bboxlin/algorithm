# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def reverseLinkedList(node):
            prev = None
            while node:
                nxtnode = node.next
                node.next = prev
                prev = node
                node = nxtnode
            return prev
        
        def getMidNode(node):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
            
  
        midnode = getMidNode(head)
        # Cut Link
        head2 = midnode.next 
        midnode.next = None 
        
        head2 = reverseLinkedList(head2)

        cur = ListNode(next=head)
        first = head
        second = head2
        while first or second:
            if first:
                cur.next = first
                first = first.next 
                cur = cur.next 
            if second:
                cur.next = second
                second = second.next 
                cur = cur.next
            