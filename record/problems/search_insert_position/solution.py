class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        pos = -1
        while l <= r:
            mid = l+r >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                pos = mid
                r = mid - 1
            else:
                pos = l+1
                l = mid + 1
        return pos