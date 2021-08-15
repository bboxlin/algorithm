# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            que = collections.deque([(root,1)])
            while que:
                node, depth  = que.popleft()
                if not node.left and not node.right:  # who first reach to a level that has not left and right, it is the min depth
                    return depth
                if node.left:
                    que.append((node.left, depth + 1))
                if node.right:
                    que.append((node.right, depth+1)) 
        if root == None: return 0        
        return bfs(root)
         
#         def dfs(root):
#             if root == None: return 0
#             left = dfs(root.left)
#             right = dfs(root. right)
#             # case for skewed tree
#             if left == 0 or right == 0: 
#                 return 1 + max(left,right)

#             return 1 + min(left,right)
        
#         if root == None: return 0
#         return dfs(root)