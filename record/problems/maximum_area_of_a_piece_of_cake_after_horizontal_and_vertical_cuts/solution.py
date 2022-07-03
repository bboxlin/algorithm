class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontals = [0] + sorted(horizontalCuts) + [h]
        verticals = [0] + sorted(verticalCuts) + [w]  
        max_height, max_width = 0, 0
        
        for i in range(1, len(horizontals)):
            max_height = max(max_height, horizontals[i] - horizontals[i-1])
            
        for i in range(1, len(verticals)):
            max_width = max(max_width, verticals[i] - verticals[i-1])
        
        return max_height * max_width % (10**9+7)
         
        