class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, ans):
            if len(nums) >= i and len(ans) >= 2: res.append(ans.copy())
            used = set() 
            for idx in range(i, len(nums)):
                if len(ans) > 0 and ans[-1] > nums[idx]: continue 
                if nums[idx] in used: continue
                used.add(nums[idx])
                ans.append(nums[idx])
                dfs(idx+1, ans)
                ans.pop()
 
        res = []
        dfs(0, [])
        return res