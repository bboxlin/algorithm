class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        ans = 0
        n = len(nums)
        
        nums.sort()
        for i in range(n-2):
            lo = i + 1
            hi = n - 1
            
            while lo < hi:
                cursum = nums[i] + nums[lo] + nums[hi]
                curdiff = abs(target - cursum)
                # match
                if curdiff == 0:
                    return cursum
                
                # closer
                if curdiff < diff:
                    diff = curdiff
                    ans = cursum
                
                # shift pointers
                if cursum < target:
                    lo += 1
                else:
                    hi -= 1
        return ans