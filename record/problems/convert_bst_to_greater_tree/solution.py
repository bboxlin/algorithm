# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.acc = 0
        def dfs(root):
            if not root: return 
            dfs(root.right)
            self.acc += root.val
            root.val = self.acc 
            dfs(root.left)
        dfs(root)
        return root