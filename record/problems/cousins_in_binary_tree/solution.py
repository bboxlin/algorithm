# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def traverse(root, depth, parent):
            if not root:
                return
            if root.val == x:
                self.x_depth = depth
                self.x_parent = parent
            if root.val == y:
                self.y_depth = depth
                self.y_parent = parent
            traverse(root.left, depth+1, root)
            traverse(root.right, depth+1, root)

        self.x_depth, self.y_depth = 0, 0
        self.x_parent, self.y_parent = None, None
        traverse(root, 0, None)
        return self.x_depth == self.y_depth and self.x_parent != self.y_parent