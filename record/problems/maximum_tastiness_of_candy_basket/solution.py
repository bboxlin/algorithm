
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # isKcandies check if there is K candies with 
        # atleast d tastiness apart. 
        def isKcandies(d):
            cnt = 0
            prev = -math.inf
            for p in price:
                if p >= prev + d:
                    cnt += 1
                    prev = p
            return cnt >= k
             

        # we want to search for maximum tastiness = right most
        price.sort() 
        l = 0 
        r = max(price) - min(price)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if isKcandies(mid):
                ans = mid 
                l = mid + 1
            else:
                r = mid - 1
        return ans 

