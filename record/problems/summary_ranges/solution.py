class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        l = 0
        while l < n:
            r = l + 1
            while r < n and nums[r] == nums[r-1] + 1:
                r += 1
            if nums[l] != nums[r-1]:
                res.append(
                    str(nums[l]) + '->' + str(nums[r-1])
                )
            else:
                res.append(
                    str(nums[l])
                )
            l = r 
        return res