class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, acc):
            res.append(acc.copy())
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue 
                acc.append(nums[i])
                dfs(i+1,acc)
                acc.pop()
        nums.sort()
        res = []
        dfs(0, [])
        return res