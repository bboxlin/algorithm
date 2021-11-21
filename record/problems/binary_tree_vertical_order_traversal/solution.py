# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root: return res
        q = collections.deque([(root, 0)])
        memo = defaultdict(list)
        
        while q:
            level_size = len(q)
            for i in range(level_size):
                node, px = q.popleft()
                memo[px].append(node.val)

                left = node.left
                right = node.right
                if left: 
                    q.append((left, px-1))
                if right: 
                    q.append((right, px+1 ))
        
        for k, v in sorted(memo.items()):
            res.append(v)
        return res

                    
            
        