# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(root, acc):
            if root:
                if not root.left and not root.right:
                    acc += str(root.val)
                    res.append(acc)
                    return
                else:
                    acc += str(root.val) + "->"
                    dfs(root.left, acc)
                    dfs(root.right, acc)
        
        res = []
        dfs(root, "")
        print(res)
        return res