"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path = set()
        while q:
            path.add(q)
            q = q.parent   
        while p:
            if p in path:
                return p
            p = p.parent
        return None