"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return
        
        def dfs(curNode):
            nonlocal prev
            if not curNode: 
                return
            dfs(curNode.left)
            prev.right = curNode
            curNode.left = prev
            prev = curNode
            dfs(curNode.right)
        
        
        dummy = Node(-1)
        prev = dummy
        dfs(root)
        
        # head tail connection
        prev.right = dummy.right
        dummy.right.left = prev
        
        return dummy.right
            