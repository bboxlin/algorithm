# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:        
        def dfs(root1, root2):
             
            if not root1: return root2
            if not root2: return root1
            
            root3 = TreeNode(root1.val+root2.val)
            root3.left = dfs(root1.left, root2.left)
            root3.right = dfs(root1.right, root2.right)
            return root3
        
        return dfs(root1,root2)