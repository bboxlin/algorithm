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

    def postorderTraversal(self, root):
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return res
    
    '''
    --------------------------- Recursive ------------------------------------------
    '''
    
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def postorder(root):
#             if not root:
#                 return root
                
#             postorder(root.left)
#             postorder(root.right)
#             if root:
#                 res.append(root.val)
            
#             return root
#         postorder(root)
#         return res