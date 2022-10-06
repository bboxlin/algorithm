import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.cache
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            mincnt = math.inf
            for coin in coins:
                cnt = dfs(amount - coin)
                if cnt == -1: continue
                mincnt = min(mincnt, cnt + 1)
            return mincnt if mincnt != math.inf else -1
        return dfs(amount)
