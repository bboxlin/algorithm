# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal res
            nonlocal prev
            if not node:
                return 
            dfs(node.left)
            res = min(res, abs(node.val - prev))
            prev = node.val
            dfs(node.right)
        
        res = math.inf
        prev = math.inf
        dfs(root)
        return res