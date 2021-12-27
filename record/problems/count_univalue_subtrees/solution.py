# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root):

        def helper(root):
            if not root: return (0, True)
            left_count, isLeft_uni = helper(root.left)
            right_count, isRight_uni = helper(root.right)
            
            # if one sub is not uni then not uni
            is_uni = isLeft_uni and isRight_uni
            
            # check cur node and sub node val
            if root.left and root.left.val != root.val:
                is_uni = False
            if root.right and root.right.val != root.val:
                is_uni = False
            
            if is_uni:
                return (left_count+right_count+1, True)
            else:
                return (left_count+right_count, False)
        
        total, is_uni = helper(root)
        return total
            