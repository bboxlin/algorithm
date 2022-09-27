# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node, lowerBound=-inf, upperBound=inf):
            if not node:
                return True
            if not lowerBound < node.val < upperBound:
                return False
            
            isLeftValid = dfs(node.left, lowerBound, node.val)
            isRightValid = dfs(node.right, node.val, upperBound)
            
            return isLeftValid and isRightValid
        
        return dfs(root)
            