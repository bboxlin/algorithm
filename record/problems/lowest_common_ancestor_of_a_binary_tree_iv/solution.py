# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':  
        nodes = set(nodes)
        
        def dfs(node):
            if not node:
                return node
            if node in nodes:
                return node
            leftnode = dfs(node.left)
            rightnode = dfs(node.right)
            
            if leftnode and rightnode: return node
            if leftnode is None: return rightnode
            if rightnode is None: return leftnode
        
        return dfs(root)
            
            