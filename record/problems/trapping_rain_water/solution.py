class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        acc = 0
        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                acc += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                acc += rMax - height[r]
        return acc