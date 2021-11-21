# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        q = collections.deque([root])
        while q:
            level_size = len(q)
            level = []
            for i in range(level_size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    left = node.left
                    right = node.right
                    if left:
                        q.append(left)
                    if right:
                        q.append(right)
            res.append(level)
        return res