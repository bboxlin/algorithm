class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0 
        p = 1
        ans = 0
        for r in range(n):
            p = p * nums[r]
            while p >= k and l <= r:
                p = p // nums[l]
                l += 1
            ans += r - l + 1
        return ans
