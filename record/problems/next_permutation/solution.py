class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
               
        def reverse_arr(i, j):
            while i < j:
                swap(i, j)
                i += 1
                j -= 1
        
        if len(nums) == 1: 
            return
        
        pos = len(nums) - 2
        while pos >= 0 and nums[pos] >= nums[pos+1]:
            pos -= 1
        
        if pos < 0:
            reverse_arr(0, len(nums)-1)
        else:
            for i in range(len(nums) - 1, pos, -1):
                if nums[i] > nums[pos]:
                    swap(i, pos)
                    break
            reverse_arr(pos+1, len(nums) - 1)
        
         
            
        
    
            
            
            
        
