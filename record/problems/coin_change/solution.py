
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            
            if amount in memo: return memo[amount]
            
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            
            mincnt = float('inf')
            for coin in coins:
                cnt = dfs(amount - coin)
                if cnt == -1:
                    continue
                mincnt = min(mincnt, cnt + 1)
            memo[amount] = mincnt if mincnt != float('inf') else -1
            return memo[amount]
        
        return dfs(amount)
