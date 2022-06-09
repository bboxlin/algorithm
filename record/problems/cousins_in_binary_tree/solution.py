# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xinfo, yinfo = [], []
        def dfs(root, pnode, depth):
            if not root:
                return 
            if root.val == x: 
                xinfo.append(pnode)
                xinfo.append(depth)
            if root.val == y:
                yinfo.append(pnode)
                yinfo.append(depth)
            dfs(root.left, root, depth+1)
            dfs(root.right, root, depth+1)
        dfs(root, None, 0)
        if len(xinfo) == 0 or len(yinfo) == 0: return False
        return xinfo[0] != yinfo[0] and xinfo[1] == yinfo[1]