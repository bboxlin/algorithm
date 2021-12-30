# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     def insert(root):
    #         if not root:
    #             return TreeNode(val)
    #         elif root.val > val:
    #             root.left = insert(root.left)
    #         else:
    #             root.right = insert(root.right)
    #         return root
    #     return insert(root)
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        while cur:
            if cur.val > val:
                if not cur.left: 
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
            else:
                if not cur.right: 
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right 
        
        return TreeNode(val)