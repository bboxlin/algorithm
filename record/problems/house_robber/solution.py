class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        total = 0
        for i in range(len(nums)):
            if i == 0:
                a = nums[i]
                total = a
            elif i == 1:
                b = max(a, nums[i])
                total = b
            else:
                total = max(a + nums[i], b)
                a = b
                b = total 
        return total                
                

class Solution2:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i, num in enumerate(nums):
            if i == 0: dp[i] = num                    # base case 1
            elif i == 1: dp[i] = max(dp[i-1], num)    # base case 2
            else:
                dp[i] = max(dp[i-1], dp[i-2]+num)
        return dp[-1]
        
