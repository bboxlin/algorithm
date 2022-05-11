class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        maxarea = 0
        while i < j:
            area = (j-i)*min(height[i], height[j])
            maxarea = max(maxarea, area)
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return maxarea