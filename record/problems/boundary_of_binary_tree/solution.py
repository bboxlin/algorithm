# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.ans = []

    def addLeftBoundary(self, node):
        if not node or (not node.left and not node.right):
            return 
        self.ans.append(node.val)
        if not node.left:
            self.addLeftBoundary(node.right)
        else:
            self.addLeftBoundary(node.left)
    
    def addLeafBoundary(self, node):
        if not node:
            return 
        if not node.left and not node.right:
            self.ans.append(node.val)
            return 
        self.addLeafBoundary(node.left)
        self.addLeafBoundary(node.right)
    
    def addRightBoundary(self, node):
        if not node or (not node.left and not node.right):
            return 
        if not node.right:
            self.addRightBoundary(node.left)
        else:
            self.addRightBoundary(node.right)
        self.ans.append(node.val)
        
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.ans.append(root.val)
        self.addLeftBoundary(root.left)
        self.addLeafBoundary(root.left)
        self.addLeafBoundary(root.right)
        self.addRightBoundary(root.right)
        return self.ans
    
    
 