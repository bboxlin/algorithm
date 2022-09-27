# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        
        def setMaxDiameter(node):
            if not node:
                return 0
            lheight = setMaxDiameter(node.left)
            rheight = setMaxDiameter(node.right)
            nonlocal d
            d = max(d, lheight + rheight)
            return max(lheight, rheight) + 1      
        d = 0    
        setMaxDiameter(root)
        return d