class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        l, r = 0, n-1
        for i in range(n-1, -1, -1):
            leftmost = nums[l]
            rightmost = nums[r]
            if abs(leftmost) > abs(rightmost):
                res[i] = leftmost**2
                l += 1
            else:
                res[i] = rightmost**2
                r -= 1
        return res
                
        
            
