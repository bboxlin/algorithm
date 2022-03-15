class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        greatest = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        size = truckSize
        res = 0
        for num, unit in greatest:
            boxcnt = min(num, size)
            res += boxcnt * unit
            size -= boxcnt
            if size <= 0: break
        return res
            
        