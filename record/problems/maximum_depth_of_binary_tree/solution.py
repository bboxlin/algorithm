# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.maxDepth = 0
        
        def dfs(root, depth):
            if not root: return
            self.maxDepth = max(self.maxDepth, depth)    
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
            
        dfs(root, 1)
        return self.maxDepth