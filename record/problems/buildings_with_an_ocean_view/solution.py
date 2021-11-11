class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # ocean at right
        
        rightMaxHeight = 0
        res = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > rightMaxHeight:
                res.append(i) 
                rightMaxHeight = heights[i]
        res.sort()
        return res