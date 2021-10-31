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
            

  