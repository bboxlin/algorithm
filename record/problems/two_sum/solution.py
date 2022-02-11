class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        memo = {}
        for i, n in enumerate(nums):
            rem = target - n
            if rem in memo:
                return [i, memo[rem]]
            else:
                memo[n] = i
        return None