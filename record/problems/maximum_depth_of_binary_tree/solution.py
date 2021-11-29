# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        maxdepth = 0
        
        def dfs(root, depth):
            
            nonlocal maxdepth
            if not root:
                maxdepth = max(maxdepth, depth)
                return root
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)
        return maxdepth