# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        
        def dfs(node, level, res):
            if not node:
                return node
            if len(res) <= level:
                res += [[]]
            dfs(node.left, level+1, res)
            dfs(node.right, level+1, res)
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0,node.val)
        
        dfs(root, 0, res)
        return res