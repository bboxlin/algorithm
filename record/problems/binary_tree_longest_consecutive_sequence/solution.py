# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, prevval, cnt):
            if not node: return 
            cnt = cnt + 1 if node.val - prevval == 1 else 1
            self.ans = max(self.ans, cnt)
            dfs(node.left, node.val, cnt)
            dfs(node.right, node.val, cnt)
        
        self.ans = 1
        dfs(root, root.val, 1)
        return self.ans