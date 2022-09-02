# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxval):
            if not node: return 
            if node.val >= maxval:
                self.good += 1
            maxval = max(node.val, maxval)
            dfs(node.left, maxval)
            dfs(node.right, maxval)
        
        
        self.good = 0 
        dfs(root, -inf)
        return self.good
        
        
        