# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node: return
            
            if node == p or node == q:
                return node
            
            leftnode = dfs(node.left) 
            rightnode = dfs(node.right)

            if leftnode and rightnode: return node
            return leftnode or rightnode
            # if leftnode is None: return rightnode
            # if rightnode is None: return leftnode
            
            return null
        
        return dfs(root)
             