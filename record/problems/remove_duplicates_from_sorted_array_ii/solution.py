class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num != nums[i-2]:
                nums[i] = num
                i += 1
        return i
"""
[1, 1, 1, 2, 2, 3]   num=1   i=0
[1, 1, 1, 2, 2, 3]   num=1   i=1
[1, 1, 1, 2, 2, 3]   num=1   i=2
[1, 1, 2, 2, 2, 3]   num=2   i=2
[1, 1, 2, 2, 2, 3]   num=2   i=3
[1, 1, 2, 2, 3, 3]   num=3   i=4
"""
               