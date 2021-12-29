# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:return
            dfs(root.left)
            if self.prev: self.min_diff = min(self.min_diff, root.val - self.prev.val)
            self.prev = root
            dfs(root.right)
        self.prev = None
        self.min_diff = math.inf
        dfs(root)
        return self.min_diff
        