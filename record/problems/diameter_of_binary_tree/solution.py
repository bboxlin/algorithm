# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def dfs(root):
            if not root:
                return 0
            maxLeftDepth = dfs(root.left)
            maxRightDepth = dfs(root.right)
            self.diameter = max(maxLeftDepth+maxRightDepth, self.diameter)
            return 1 + max(maxLeftDepth,maxRightDepth)
        dfs(root)
        return self.diameter