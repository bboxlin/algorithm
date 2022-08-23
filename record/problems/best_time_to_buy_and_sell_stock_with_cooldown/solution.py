class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_hold = [0] * n 
        dp_sell = [0] * n 
        dp_cool = [0] * n 
        for i in range(n):
            if i == 0:
                dp_hold[i] -= prices[i]
                dp_sell[i] = -inf
                dp_cool[i] = 0 
            else:
                dp_hold[i] = max(dp_hold[i-1], dp_cool[i-1] - prices[i])  
                dp_sell[i] = dp_hold[i-1] + prices[i]
                dp_cool[i] = max(dp_cool[i-1], dp_sell[i-1])
        return max(dp_cool[n-1], dp_sell[n-1])