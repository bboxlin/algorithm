# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        
        def build(inorder, postorder):
            if not inorder or not postorder:
                return None
            
            val = postorder[-1]
            node = TreeNode(val)
            partition = inorder.index(val)
            
            node.left = build(inorder[:partition], postorder[:partition])
            node.right = build(inorder[partition+1:], postorder[partition:-1])
             
            
            return node
        return build(inorder, postorder)
