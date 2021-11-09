# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        l, r = 0, len(nums)-1
        def dfs(l ,r):
            if l > r: 
                return None
            mid = (l+r) >> 1
            root = TreeNode(nums[mid])
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1, r)
            
            return root #return, post fix
        return dfs(l,r)
    
    
    # [-10,-3,0,5,9]
    # 0.left  -10 
    # 0.right
    
                    