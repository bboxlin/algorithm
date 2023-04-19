# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, dir=None):
            if not node:
                return 0
            leftmax = dfs(node.left, 'l')
            rightmax = dfs(node.right, 'r')
            # suppose each node returns its max Zigzag path from itself 
            # to the leaf.
            mymax = 0
            if dir == 'l': mymax = rightmax + 1
            if dir == 'r': mymax = leftmax + 1
            self.res = max(self.res, mymax)
            return mymax
        self.res = 0
        dfs(root)
        return self.res
