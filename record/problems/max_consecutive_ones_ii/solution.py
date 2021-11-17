class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r, res = 0,0,0
        aZero = False
        while r < len(nums):
            if not aZero:
                if nums[r] == 0:
                    aZero = True
                r += 1
            elif nums[r] == 1:
                r += 1
            else: # ...0
                if nums[l] == 0:
                    aZero = False
                l += 1
            res = max(res, r-l)
        return res