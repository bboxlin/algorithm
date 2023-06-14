# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    node
 Left   Right

 res = min(res, node.val - leftmax, rightmin - node.val) 
"""
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = math.inf
        def dfs(node):
            if not node:
                # we want (min, max)
                return (math.inf, -math.inf)
            leftmin, leftmax = dfs(node.left)
            rightmin, rightmax = dfs(node.right)
            nonlocal res
            res = min(res, node.val - leftmax, rightmin - node.val)
            submin = min(leftmin, rightmin, node.val)
            submax = max(leftmax, rightmax, node.val)
            return (submin, submax)
        dfs(root)
        return res