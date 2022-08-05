class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
  
        res = []
        def dfs(i, rem, arr):       
            if rem == 0:
                res.append(arr.copy())
            if rem < 0:
                return 
            
            for idx in range(i, len(candidates)):
                arr.append(candidates[idx])
                dfs(idx, rem -candidates[idx], arr)
                arr.pop()
                    
        dfs(0, target, [])
        return res
       
        
        