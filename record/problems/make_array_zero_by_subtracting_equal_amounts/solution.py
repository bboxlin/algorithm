class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        while sum(nums) > 0:
            
            minval = min([ n for n in nums if n > 0])

            for i in range(n):
                if nums[i] > 0:
                    nums[i] = nums[i] - minval 
            res += 1

        return res
        