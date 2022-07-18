# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        def dfs(root, summ):
            if not root:
                return 
            
            summ += root.val 
            if summ == targetSum:
                self.cnt += 1
            
            self.cnt += lookup[summ - targetSum]
            # self.cnt += lookup[targetSum - summ]
            lookup[summ] += 1
            
            
            dfs(root.left, summ)
            dfs(root.right, summ)
            lookup[summ] -= 1
            
        self.cnt = 0    
        lookup = collections.defaultdict(int)
        dfs(root, 0)
        return self.cnt