class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # l v1 v2 v3 r
        # subsequence between l to r
        # for each value other than l, we can either pick or not pick 
        # so numbers of way will be 2^(r-l)
        mod = 10**9 + 7
        res = 0
        nums.sort()
        n = len(nums)
        r = n - 1
        for l in range(n):
            while r >= 0 and nums[l] + nums[r] > target:
                r -= 1
            if r < l: break
            res += 2**(r-l)
            res = res % mod
        return res 

