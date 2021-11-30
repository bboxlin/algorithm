# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        in_order = []
        
        def inorder(root):
            if not root:
                return root
            inorder(root.left)
            in_order.append(root.val)
            inorder(root.right)    
        inorder(root)
        
        def build_tree(l, r):
            if l > r:
                return None
            mid = l+r >> 1
            node = TreeNode(in_order[mid])
            node.left = build_tree(l, mid-1)
            node.right = build_tree(mid+1, r)
            return node
        
        newroot = build_tree(0, len(in_order)-1)
        
        return newroot