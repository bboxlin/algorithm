class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, one_solution, cur_value):       
            if cur_value < 0 or i >= len(candidates): return
            if cur_value == 0:
                res.append(one_solution.copy())
                return
            one_solution.append(candidates[i])
            dfs(i, one_solution, cur_value - candidates[i])
            one_solution.pop()
            dfs(i+1, one_solution, cur_value)
        dfs(0,[],target)
        return res
       
        
        