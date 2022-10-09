# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def dfs(root):
            if not root:
                return 
            
            rem = k - root.val 
            if rem in seen:
                self.ans = True
            seen.add(root.val)
            dfs(root.left)
            dfs(root.right)
        
        self.ans = False
        seen = set()
        dfs(root)
 
        return self.ans
            
            