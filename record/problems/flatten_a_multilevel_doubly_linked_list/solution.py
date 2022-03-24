"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
       
        def get_tail(node):
            cur = node
            while cur and cur.next:
                cur = cur.next
            return cur
    
        cur = head
        while cur:
            if cur.child:
                # adjust child and current pointers
                tmp_next = cur.next
                cur.next = cur.child
                cur.child.prev = cur
                
                child_tail = get_tail(cur.child)
                
                if tmp_next:
                    tmp_next.prev = child_tail
                child_tail.next = tmp_next
                
                cur.child = None
            cur = cur.next
        return head
        