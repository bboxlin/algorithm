class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = max(prices)
        for price in prices:
            minprice = min(price, minprice)
            maxprofit = max(price-minprice, maxprofit)
        return maxprofit