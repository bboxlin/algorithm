# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # [0,0,0,1,0,0,2,2,2]
#         # [2,2,2,1,0,0,0,0,0]
#         #  i         l
#         #  s
#         n = len(nums)
#         s, l = 0, n-1
#         i = 0
#         while i <= l:
#             while i <= l and nums[i] == 2:
#                 nums[i], nums[l] = nums[l], nums[i]
#                 l-=1
                
#             if nums[i] == 0:
#                 nums[i], nums[s] = nums[s], nums[i]
#                 s+=1 
#             i+=1
                
    
    
#         #[2 1 2]
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, l = 0, 0
        r = len(nums) - 1
        while l <= r:
            while l <= r and nums[l] == 2:
                nums[r], nums[l] = nums[l], nums[r]
                r -= 1
            if nums[l] == 0:
                nums[i], nums[l] = nums[l], nums[i] #swap
                i += 1
            l += 1