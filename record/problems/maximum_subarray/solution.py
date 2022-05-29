class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = [0]*len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i - 1])
        # return max(dp)
    
        finalMax = nums[0];
        tempMax = 0;
        for num in nums:
            tempMax = max(tempMax+num, num)
            finalMax = max(finalMax, tempMax)
        return finalMax