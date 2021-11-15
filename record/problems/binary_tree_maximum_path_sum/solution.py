# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:  
        maxval = [float('-inf')]
        def dfs(node):
            if not node: 
                return 0 
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right)) 
            maxval[0] = max(left + right + node.val, maxval[0])
            return node.val + max(left, right)
        dfs(root)
        return maxval[0]