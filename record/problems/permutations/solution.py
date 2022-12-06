class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(acc):
            if len(acc) == len(nums):
                res.append(acc.copy())
                return 
            for num in nums:
                if num in set(acc): 
                    continue
                acc.append(num)
                dfs(acc)
                acc.pop()                   
        dfs([])
        return res