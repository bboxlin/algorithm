class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0];
        prevSubArraySum = 0;
        for num in nums:
            curSubArraySum = prevSubArraySum + num
            prevSubArraySum = max(curSubArraySum, num)
            maxSum = max(maxSum, prevSubArraySum)
        return maxSum