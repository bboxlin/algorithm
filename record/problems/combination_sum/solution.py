class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(idx, rem, acc):
            if rem == 0:
                res.append(acc.copy())
                return 
            if rem < 0:
                return 
            for i in range(idx, len(candidates)):
                acc.append(candidates[i])
                dfs(i, rem-candidates[i], acc)
                acc.pop()

        res = []
        dfs(0, target, [])
        return res