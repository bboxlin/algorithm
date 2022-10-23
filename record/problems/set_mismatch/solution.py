class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1+2..+n 
        total = n*(n+1) // 2
        curtotal = sum(nums)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dup = nums[i]
                remain = curtotal - dup
                missVal = total - remain
                return [dup,missVal]
                
         
 