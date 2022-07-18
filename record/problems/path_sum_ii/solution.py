# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, total, acc):
            if root is None:
                return   
            total += root.val
            acc.append(root.val)
            if not root.left and not root.right and total == targetSum:
                ans.append(acc[:])
            dfs(root.left, total, acc)
            dfs(root.right, total, acc)
            acc.pop()
        ans = []
        dfs(root, 0,[])
        return ans
 
    