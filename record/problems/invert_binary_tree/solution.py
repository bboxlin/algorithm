# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        leftnode = self.invertTree(root.left)
        rightnode = self.invertTree(root.right)
        
        root.left = rightnode
        root.right = leftnode
        
        return root