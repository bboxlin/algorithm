class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i, n in enumerate(nums):
            rightsum = total - leftsum - nums[i]
            if leftsum == rightsum:
                return i
            leftsum += n
        return -1             
                                 