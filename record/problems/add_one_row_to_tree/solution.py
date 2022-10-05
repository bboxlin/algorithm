# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def dfs(root,d):
            if not root:
                return 
            if d+1 == depth:
                newleft = TreeNode(val=val)
                newright = TreeNode(val=val)
                
                oldleft = root.left 
                oldright = root.right 
                
                root.left = newleft
                root.right = newright 
                
                newleft.left = oldleft
                newright.right = oldright
                
            dfs(root.left, d+1)
            dfs(root.right, d+1)
            
        if depth == 1:
            newroot = TreeNode(val=val)
            newroot.left = root
            return newroot
            
            
            
        dfs(root, 1)
        return root