class Solution:
    def search(self, nums: List[int], target: int) -> int:  
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            # 如果不等于是不是需要判断当前的nums[mid]属于左边还是右边的排好序的subarr 
            # 属于左边盘好序的
            if nums[l] <= nums[mid]:
                # 如果target不在 left -- mid 这一区间已经sorted arr里 target肯定在另外一边 
                if not nums[l] <= target < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
 
            # 属于右边拍好序的
            else:
                if not nums[mid] < target <= nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return l if nums[l] == target else -1
                
                