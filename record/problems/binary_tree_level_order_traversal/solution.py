# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root: return levels     
        def dfs(root, depth):
            if not root: return
            if depth == len(levels):
                levels.append([])
            levels[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)
        return levels