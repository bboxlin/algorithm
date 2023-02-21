class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, len(nums) - 1 
        while l <= r:
            m = (l+r) // 2
            if (m - 1 < 0 or nums[m-1] != nums[m]) and (m + 1 == n or nums[m+1] != nums[m]):
                return nums[m]
            leftcnt = m - 1 if nums[m-1] == nums[m] else m
            if leftcnt % 2 != 0:
                r = m - 1 
            else:
                l = m + 1
        return -1