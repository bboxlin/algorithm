class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        ans = -1
        while l < r:
            mid = l + r >> 1
            # we are at left sorted arr so search for right
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
 
                

        return nums[r]