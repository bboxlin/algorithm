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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        stack = [root]
        
        while stack:
            cur_node = stack.pop()
            left_node = cur_node.left
            right_node = cur_node.right
            
            res.append(cur_node.val)
            if right_node:
                stack.append(right_node)
            if left_node:
                stack.append(left_node)
        return res
    
    '''
    --------------------------- Recursive ------------------------------------------
    
        def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preorder(root):
            if not root:
                return root
            if root:
                res.append(root.val)
                
            preorder(root.left)
            preorder(root.right)
            
            return root
        preorder(root)
        return res
        
    '''
