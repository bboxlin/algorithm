# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummyHead = TreeNode()
        self.cur = dummyHead
        def dfs(root):
            if not root: return
            dfs(root.left)
            root.left = None
            self.cur.right = root
            self.cur = self.cur.right 
            dfs(root.right)
        dfs(root)
        return dummyHead.right