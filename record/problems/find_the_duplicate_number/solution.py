class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = -1
        l, r, = 1, len(nums)-1 
        while l <=r :
            mid = (l + r) // 2 
            count = 0
            for num in nums:
                if num <= mid: count+=1
            if count > mid:
                r = mid - 1 
                res = mid
            else:
                l = mid + 1
        return res
        
    

     