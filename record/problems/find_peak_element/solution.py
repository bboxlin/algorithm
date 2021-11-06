class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) >> 1
            # descending afer mid must a peek at left sub array, possibily the current mid
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1  # if ascending after mid, then peek must at right sub array, exclude the current mid possibility
        return left