# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            
            if not self.sucessor and root.val > p.val:
                self.sucessor = root
            elif self.sucessor and root.val > p.val:
                if self.sucessor.val > root.val:
                    self.sucessor = root
                    
            dfs(root.right)
        
        self.sucessor = None
        dfs(root)
        return self.sucessor