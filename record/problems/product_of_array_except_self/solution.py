class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]*len(nums)
        
        left = 1
        for i in range(1,len(nums)):
            left = left * nums[i-1]  #accumulate the left product
            res[i] = left  # assignment
        
 
        right = 1
        for i in range(len(nums)-2, -1, -1):
            right = right * nums[i+1] #accumulate the right product
            res[i] = res[i] * right # left * right 
            
        return res
                 