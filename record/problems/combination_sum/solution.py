class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            for i in range(1,target+1):
                if i < c: continue
                if i == c: dp[i].append([c])
                if i > c:
                    for sublist in dp[i-c]:
                        dp[i].append(sublist+[c])
        return dp[target]
       
        
        