# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 1]])
        res = 1
        while q:
            leftnum = -math.inf
            for i in range(len(q)):
                node, num = q.popleft()
                if i == 0: leftnum = num
                res = max(res, num-leftnum+1)
                leftnode = node.left
                rightnode = node.right
                if leftnode:
                    q.append([leftnode, 2*num])
                if rightnode:
                    q.append([rightnode, 2*num+1])
        return res
                



