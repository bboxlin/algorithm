class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        for n in nums:
            if n > lower:
                if n - lower == 1:
                    res.append(str(lower))
                else:
                    res.append(str(lower) + "->" + str(n-1))
            
            lower = n + 1
        
        if lower < upper:
            res.append(str(lower) + "->" + str(upper))
        elif lower == upper:
            res.append(str(lower))
        
        return res
                    
            