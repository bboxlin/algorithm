class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def overlap():
            if bx2 <= ax1 or bx1 >= ax2:
                return False
            if ay2 <= by1 or ay1 >= by2:
                return False
            return True
        
        
        area = (ay2 - ay1) * (ax2 - ax1) + (by2 - by1) * (bx2 - bx1)
        if overlap():
            w = min(ax2,bx2) - max(ax1, bx1) 
            h = min(ay2, by2) - max(ay1, by1)
            area -= w*h
        return area
        
            
            
        