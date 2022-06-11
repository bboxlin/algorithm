class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        windowSize = sum(nums) - x  # non-answer subarray size
        if windowSize == 0: return n
        presum = {0 : -1}
        cursum = 0
        ans = n + 1
         
        for right in range(n):
            
            cursum += nums[right]
            presum[cursum] = right 
            
            if cursum - windowSize in presum.keys():
                left = presum[cursum - windowSize]
                ans = min(ans, n - (right - left) )
    
        return -1 if ans == n + 1 else ans
