class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
 
        ans = []
        n = len(nums)
        for i in range(n):
            l, r = i + 1, n - 1 
            if nums[i] > 0: break 
            if i > 0 and nums[i] == nums[i-1]: continue 
            
            while l < r:
  
                cursum = nums[i] + nums[l] + nums[r]
                if cursum > 0:
                    r -= 1
                elif cursum < 0:
                    l += 1
                else:
                    ans.append( [nums[i], nums[l], nums[r]] )
                    
                    """
                    These two while loop can only be here, since current ans is record we can skip for duplicate
                    """
         
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1 
                    r -= 1
                     
                
                 
        return ans