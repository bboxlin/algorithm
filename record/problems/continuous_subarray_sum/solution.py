class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # rem : index
        memo = {0 : -1}
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            rem = cursum % k
            if rem in memo and i - memo[rem] > 1 :
                return True
            if rem not in memo:
                memo[rem] = i
        return False
    

