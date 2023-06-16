class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        def dfs(nums):
            m = len(nums)
            if m < 3: 
                return 1
            curNode = nums[0]
            leftTree = [a for a in nums if a < curNode]
            rightTree = [a for a in nums if a > curNode]
            return dfs(leftTree) * dfs(rightTree) * comb(len(leftTree) + len(rightTree) , len(leftTree)) % mod
        
        return (dfs(nums) - 1) % mod