class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxdp, mindp = [0]*n, [0]*n
        for i in range(n):
            if i == 0: 
                maxdp[i] = nums[i]
                mindp[i] = nums[i] 
            else:
                maxdp[i] = max(maxdp[i-1] * nums[i], mindp[i-1] * nums[i], nums[i])
                mindp[i] = min(maxdp[i-1] * nums[i], mindp[i-1] * nums[i], nums[i])
                
        return max(maxdp)

    # def maxProduct(self, nums: List[int]) -> int:
    #     ans = max(nums)
    #     maxprod, minprod = 1, 1
    #     for n in nums:
    #         maxprod, minprod = max(maxprod * n, minprod * n, n), min(maxprod * n, minprod * n, n)
    #         ans = max(maxprod, ans)
    #     return ans
       