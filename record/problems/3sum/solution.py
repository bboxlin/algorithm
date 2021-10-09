class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if not nums or n<3: return []
        nums.sort()
        
        for i in range(n):
            if nums[i] > 0: return res 
            if i > 0 and nums[i] == nums[i-1]: continue
            l = i+1
            r = n-1
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0: 
                    res.append([nums[i], nums[l], nums[r]])
                    while (l<r and nums[l] == nums[l+1]): 
                        l=l+1
                    while (l<r and nums[r] == nums[r-1]):
                        r=r-1
                    l=l+1
                    r=r-1
                elif nums[i] + nums[l] + nums[r] > 0:r=r-1
                else: l=l+1
                    
        return res
                    
                