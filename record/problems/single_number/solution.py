class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # O(n) run time, O(1) space
        repeat = 0
        for num in nums:
            repeat = repeat^num
        return repeat