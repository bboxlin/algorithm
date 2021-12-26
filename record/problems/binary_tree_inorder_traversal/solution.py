# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    '''
    -------------------------- Iterative ----------------------------------------------
    '''
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         stack, res = [], []
#         if not root: return res

#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left    
#             root = stack.pop()
#             res.append(root.val)
#             root = root.right
#         return res
    
    '''
    --------------------------- Recursive ------------------------------------------
    '''
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return root
                
            inorder(root.left)
            if root:
                res.append(root.val)
            inorder(root.right)
            
            return root
        inorder(root)
        return res
        
  