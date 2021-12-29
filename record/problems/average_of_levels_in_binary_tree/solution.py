# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
         
        
        def dfs(root,depth):
            if not root:
                return
            if depth not in subtotal.keys():
                subtotal[depth] = [root.val, 1]
            else:
                subtotal[depth][0] += root.val
                subtotal[depth][1] += 1
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
            
        subtotal = collections.defaultdict(list)
        dfs(root, 0)
        res = []
        for v in subtotal.values():
            subtotal, count = v
            res.append(subtotal/count)
         
        return res