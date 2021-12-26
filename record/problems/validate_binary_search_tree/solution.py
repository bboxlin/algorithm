# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lower, upper):
            if not root:
                return True
            
            if root.val <= lower or root.val >= upper:
                return False
            
            left_valid = dfs(root.left, lower, root.val)
            right_valid = dfs(root.right, root.val, upper)
            
            return left_valid and right_valid
            
        return dfs(root, -math.inf, math.inf)