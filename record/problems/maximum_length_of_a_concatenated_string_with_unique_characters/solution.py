class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def dfs(pos, s):
            if len(s) != len(set(s)):
                return 0
            ans = len(s)
            for i in range(pos, len(arr)):
                ans = max(ans, dfs(i+1, s+arr[i]))
            return ans
        
        return dfs(0, "")