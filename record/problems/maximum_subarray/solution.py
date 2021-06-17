class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        finalMax = nums[0];
        tempMax = 0;
        for num in nums:
            tempMax = max(tempMax+num, num)
            if tempMax > finalMax:
                finalMax = tempMax
        return finalMax
                    