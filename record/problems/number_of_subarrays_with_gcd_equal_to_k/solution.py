from math import gcd
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == k:
                    cnt += 1
        return cnt