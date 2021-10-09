class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        n = len(nums)
        nums.sort()
        
        for i in range (n):
            l = i+1
            r = n-1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if abs(target - ans) > abs(target - res):
                    ans = res
                elif res < target: l+=1
                elif res > target: r-=1
                else:
                    return ans #ans = target
        return ans
        