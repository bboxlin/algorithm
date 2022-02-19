class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        # handle the horizontal part
        if rec2[0] >= rec1[2] or rec1[0] >= rec2[2]: return False
        
        # handle the vertical part 
        if rec2[1] >= rec1[3] or rec1[1] >= rec2[3]: return False
        
        return True
        
        # left = max(rec1[0], rec2[0])
        # right = min(rec1[2], rec2[2])
        # bottom = max(rec1[1], rec2[1])
        # up  = min(rec1[3], rec2[3])
        # return right>left and up>bottom