# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
#         def dfs(root):
#             if not root: return
#             print(root.val, self.cnt)
#             dfs(root.left)
#             self.cnt += 1
#             if self.cnt == k:
#                 self.ans = root.val 
          
#             dfs(root.right)
            
#         self.cnt = 0
#         self.ans = 0
#         dfs(root)
#         return self.ans
    
        stack = [root]
        while stack:
            curnode = stack.pop()
            while curnode:
                stack.append(curnode)
                curnode = curnode.left 
            smallnode = stack.pop()
            k -= 1
            if k == 0:
                return smallnode.val
            stack.append(smallnode.right)
          