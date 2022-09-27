class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        minprice = inf
        for price in prices:
            minprice = min(price, minprice)
            earn = price - minprice
            ans = max(earn, ans)
        return ans
    
    #[ 7,1,5,3,6,5 ]
    #  7 1 1 1 1 | 
    #          5
    #
    #