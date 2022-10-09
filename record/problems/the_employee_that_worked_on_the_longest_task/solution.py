class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        maxtask = 0
        ans = 0
        prev = 0
        for curid, amount in logs:
            curtask = amount - prev 
            prev = amount 
            if curtask > maxtask:
                maxtask = curtask
                ans = curid
            elif curtask == maxtask:
                ans = min(ans,curid)
        return ans
            
            
        