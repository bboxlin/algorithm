class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        if n < 3: return 0
        ans = 0
        
        # proof:
        # nums in [max............min]  reversely sorted order
        # now suppose nums[i] >= nums[i+1] + nums[i+2]
        #.        question is: is it possible that: nums[i] < nums[k+1] + nums[k+2] where k > i
        #                      NO!!
        
        for i in range(n-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0