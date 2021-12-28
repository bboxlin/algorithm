# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(root, side=None):
            if not root:
                return
            if not root.left and not root.right:
                if side == "left": 
                    self.total += root.val
                    return
                
            dfs(root.left, "left")
            dfs(root.right, "right")

        self.total = 0
        dfs(root)
        return self.total