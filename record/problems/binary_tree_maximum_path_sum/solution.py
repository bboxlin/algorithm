# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:  
        def dfs(node):
            if not node: 
                return 0 
            nonlocal ans
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right)) 
            ans = max(left + right + node.val, ans)
            return node.val + max(left, right)
        ans = -math.inf
        dfs(root)
        return ans