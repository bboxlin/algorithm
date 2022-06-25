from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, n in enumerate(nums):
            if target - n in memo.keys(): 
                return [memo[target-n], i]
            memo[n] = i
        return [-1, -1]
        