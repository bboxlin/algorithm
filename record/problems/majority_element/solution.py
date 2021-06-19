class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(i,j):
            if i == j: return nums[i]
            mid = (i+j)//2
            leftMajor = helper(i,mid)
            rightMajor = helper(mid+1,j)
            
            if leftMajor == rightMajor: return leftMajor
                
            leftCount = sum(1 for i in range(i,j+1) if nums[i] == leftMajor)
            rightCount = sum(1 for i in range(i,j+1) if nums[i] == rightMajor)
            
            return leftMajor if leftCount > rightCount else rightMajor
        
        return helper(0,len(nums)-1)
            
            
            
             
            