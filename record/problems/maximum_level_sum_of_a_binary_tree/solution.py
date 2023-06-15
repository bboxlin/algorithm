# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = math.inf
        maxLevelSum = -math.inf
        i = 1
        while q:
            levelSum = 0 
            for _ in range(len(q)):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if levelSum > maxLevelSum:
                maxLevelSum = levelSum
                res = i
            
            i += 1
        return res