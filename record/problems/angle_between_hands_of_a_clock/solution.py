class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 1 minutes = 6 degree 
        # max degree = 180 degree
#         hrdegree = hour % 12 * 30 + float(minutes/60) * 30
#         mindegree = minutes * 6 
#         angle = abs(mindegree - hrdegree)
#         if angle > 180:
#             return 360.0 - angle
#         return angle
    
        hrmin = hour % 12 * 5 + float(minutes/60) * 5
        mindiff = abs(minutes - hrmin)
        if mindiff > 30:
            return (60-mindiff)*6
        return mindiff * 6