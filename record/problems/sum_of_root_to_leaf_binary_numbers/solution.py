# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, acc):
            if root:
                # add
                acc = (acc << 1) | root.val
                if not root.left and not root.right:
                    self.total += acc
                dfs(root.left, acc)
                dfs(root.right, acc)
        self.total = 0
        dfs(root, 0)
        return self.total