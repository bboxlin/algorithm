# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    preorder的首位数是tree/subtree的root, 依次寻找其在inorder的位置则判断出该位置往左都是left subtree, etc..
    可观, 其数在inorder的位置之距是preorder首位数之后若干位的左子树, 递归可成
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def build(preorder, inorder):
            if not preorder and not inorder:
                return None
            val = preorder[0]
            node = TreeNode(val)
            partition = inorder.index(val)
            
            node.left = build(preorder[1:partition+1], inorder[:partition])
            node.right = build(preorder[partition+1:], inorder[partition+1:])
            return node
        return build(preorder, inorder)