class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_purchase = inf
        max_profit = 0
        for n in prices:
            min_purchase = min(min_purchase, n)
            max_profit = max(n - min_purchase, max_profit)
        return max_profit