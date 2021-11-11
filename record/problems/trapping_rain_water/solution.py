class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        max_height = max(height)
        max_h_index = height.index(max_height)
        last_index = len(height) - 1
        leftMaxHeight, rightMaxHeight = height[0], height[-1]
        
        # get waters from left side of max_h_index
        for l in range(0, max_h_index):
            if height[l] > leftMaxHeight:
                leftMaxHeight = height[l]
            else:
                res += leftMaxHeight - height[l]
        
        # get waters from right side of max_h_index
        for r in range(last_index, max_h_index, -1):
            if height[r] > rightMaxHeight:
                rightMaxHeight = height[r]
            else:
                res += rightMaxHeight - height[r]
                
        return res
                
                