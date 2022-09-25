class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        ans = [] 
        n = len(nums)
        left = [1] * n 
        right = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                left[i] = 1
            else:
                left[i] = left[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                right[i] = 1
            else:
                right[i] = right[i+1] + 1
        
        for i in range(k, n-k):
            if left[i-1] >= k and right[i+1] >= k:
                ans.append(i)
        return ans
                
  
    
 
         