class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        # 思路2
        # EASY TO UNDERSTAND
        one = 0
        for i in range(n):
            if nums[i] != 0:
                nums[one] = nums[i]
                one += 1
        for i in range(one, n):
            nums[i] = 0
     
    
