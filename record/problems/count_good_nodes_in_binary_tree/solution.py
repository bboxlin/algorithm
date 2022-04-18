# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        def dfs(root, prevmax):
            if not root: return
            if root.val >= prevmax: 
                self.cnt += 1
                prevmax = root.val
            dfs(root.left, prevmax)
            dfs(root.right, prevmax)
        dfs(root, float('-inf'))
        return self.cnt