class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        try:
            start = nums[0]
        except:
            return res
        
        for i in range(len(nums)-1):
            v = nums[i+1] - nums[i]
            if v > 1:
                if start == nums[i]: 
                    res.append(str(start))
                else:
                    item = str(start) + "->" + str(nums[i])
                    res.append(item)
                start = nums[i+1]
                    
        if start == nums[-1]:
            res.append(str(start))
        else:
            item = str(start) + "->" + str(nums[-1])
            res.append(item)
            
        return res