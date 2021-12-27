"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def connected(node1, node2):
            if not node1 or not node2:
                return
            node1.next = node2
            connected(node1.left, node1.right)
            connected(node1.right, node2.left)
            connected(node2.left, node2.right)
        if not root: return root
        connected(root.left, root.right)
        return root