# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
   
        def dfs(root):
            if not root:
                return (0.0, 0)
            leftsum, leftlen = dfs(root.left)
            rightsum, rightlen = dfs(root.right)
            curtotal = leftsum + rightsum + root.val 
            lentotal = leftlen + rightlen + 1 
            curavg = float(curtotal/lentotal)
            self.max_avg = max(self.max_avg, curavg)
            return (curtotal, lentotal)
          
        self.max_avg = 0 
        dfs(root)
        return self.max_avg