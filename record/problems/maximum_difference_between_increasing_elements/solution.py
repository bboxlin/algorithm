class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if not nums: return -1
        themin = nums[0]
        ans = -1
        for n in nums:
            ans = max(ans, n - themin)
            themin = min(themin, n)
        return ans if ans != 0 else -1