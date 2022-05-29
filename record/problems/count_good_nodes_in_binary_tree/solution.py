# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.cnt = 0
        
        def dfs(root, prevMax):
            
            if not root: return
            if root.val >= prevMax:
                self.cnt += 1
                prevMax = root.val
            
            dfs(root.left, prevMax)
            dfs(root.right, prevMax)
        
        dfs(root, root.val)
        return self.cnt