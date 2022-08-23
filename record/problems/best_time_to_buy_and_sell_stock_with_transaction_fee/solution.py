class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold = [0] * n
        sold = [0] * n
        for i in range(n):
            if i == 0:
                hold[i] -= prices[i]
                sold[i] = 0
            else:
                hold[i] = max(hold[i-1], sold[i-1]-prices[i]) #昨天出售今天購入
                sold[i] = max(sold[i-1], hold[i-1]+prices[i]-fee) #今日售出
                
        return sold[n-1]