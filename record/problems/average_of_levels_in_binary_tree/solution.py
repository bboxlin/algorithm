# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        while q:
            level_len = len(q)
            curlevel_sum = 0
            for _ in range(level_len):
                node = q.popleft() 
                leftnode = node.left 
                rightnode = node.right
                if leftnode:
                    q.append(leftnode)
                if rightnode:
                    q.append(rightnode)
                curlevel_sum += node.val
            ans.append(curlevel_sum/level_len)
        return ans
            
            
            
        