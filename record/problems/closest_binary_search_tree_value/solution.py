# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def dfs(root, val):
            if not root:
                return val
            if abs(root.val - target) < abs(val - target): val = root.val
            if root.val < target: val = dfs(root.right, val)
            elif root.val > target: val = dfs(root.left, val)
            return val
        return dfs(root, root.val)