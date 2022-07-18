# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(root, acc):      
            if not root:
                return
 
            if not root.left and not root.right:
                acc = acc + str(root.val)
                self.ans.append(acc)
                
            dfs(root.left, acc + str(root.val) + "->")
            dfs(root.right, acc + str(root.val)+ "->")
        
        
        self.ans = [] 
        dfs(root, "")
        return self.ans
            