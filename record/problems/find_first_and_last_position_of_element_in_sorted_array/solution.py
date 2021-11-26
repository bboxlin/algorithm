class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums)-1    
        first = -1
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                first = mid
                r = mid - 1
        
        l, r = 0, len(nums)-1
        second = -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                second = mid
                l = mid + 1
                
        return [first,second]
                