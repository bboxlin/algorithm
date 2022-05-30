class Solution:
    # [1, 2, 3]
    # 2-1, 3-1, 3-2 = 1,2,1
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ma, mi = nums[i], nums[i]
            for j in range(i, len(nums)):
                ma = max(nums[j], ma)
                mi = min(nums[j], mi)
                ans += ma-mi
        return ans