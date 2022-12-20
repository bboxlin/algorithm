class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # the idea is to keep max and min dp as well, since we have negative number.
        n = len(nums)
        maxdp, mindp = [0]*n, [0]*n
        for i in range(n):
            if i == 0:
                maxdp[i] = nums[i]
                mindp[i] = nums[i]
            else:
                maxdp[i] = max(maxdp[i-1]*nums[i], mindp[i-1]*nums[i], nums[i])
                mindp[i] = min(maxdp[i-1]*nums[i], mindp[i-1]*nums[i], nums[i])

        return max(maxdp)