# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_exist = False
        q_exist = False
        
        def dfs(node):
            nonlocal p_exist
            nonlocal q_exist
            
            if not node:
                return node

            leftnode = dfs(node.left) 
            rightnode = dfs(node.right)
            if node == p:
                p_exist = True
                return node
            
            if node == q:
                q_exist = True
                return node
            
            if leftnode and rightnode: return node
            return leftnode or rightnode
        ans = dfs(root)
        if p_exist and q_exist:
            return ans
        return None