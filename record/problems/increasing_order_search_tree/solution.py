# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root:
                return root
            
            dfs(root.left)
            
            self.cur.right = root
            root.left = None
            self.cur = root
            
            dfs(root.right)
            
        self.dummyHead = TreeNode(-1)
        self.cur = self.dummyHead
        dfs(root)
        return self.dummyHead.right