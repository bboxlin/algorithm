class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n^2) time O(1) Space
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]: return True 
        # return False
        
        
        # O(n) time O(n) Space
        # hashset = set() 
        # for num in nums:
        #     if num in hashset:
        #         return True 
        #     hashset.add(num)
        # return False
        
        nums.sort() 
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return True 
        return False
        
        
     