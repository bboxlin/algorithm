class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
#         def dfs(idx):
#             if idx in cache:
#                 return cache[idx]
#             if idx == N-1:
#                 cache[idx] = 1
#                 return 1
#             prev = nums[idx]
#             max_len = 1
#             for i in range(idx+1, N):
#                 if nums[i] > prev:
#                     cur_len = 1 + dfs(i)
#                     max_len = max(max_len, cur_len)
#             cache[idx] = max_len
#             return max_len
        
#         cache = {}
#         N = len(nums)
#         max_len = 0
#         for i in range(N):
#             max_len = max(max_len, dfs(i))
#         return max_len
        
        dp = [1] * len(nums)
        
        for i in range(len(nums), -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)