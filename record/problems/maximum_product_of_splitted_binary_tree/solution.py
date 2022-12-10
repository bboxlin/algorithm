# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def getTotal(node):
            if not node: return 0
            leftTotal = getTotal(node.left)
            rightTotal = getTotal(node.right)
            return leftTotal + rightTotal + node.val 
        
        def trySplit(node):
            if not node:
                return 0
            nonlocal total
            nonlocal ans
            ltotal = trySplit(node.left)
            rtotal = trySplit(node.right)
            # try split with left edge 
            ans = max(ans, (total - ltotal)*ltotal)
            # try split with right edge 
            ans = max(ans, (total - rtotal)*rtotal)
            return ltotal + rtotal + node.val
        total = getTotal(root)
        ans = 0 
        trySplit(root)
        return ans % (10**9+7)

        
       