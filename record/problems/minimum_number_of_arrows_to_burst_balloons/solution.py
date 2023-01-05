class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        ans = 0
        prevend = -math.inf
        for start, end in points:
            if start > prevend:
                ans += 1
                prevend = end
        return ans
        
