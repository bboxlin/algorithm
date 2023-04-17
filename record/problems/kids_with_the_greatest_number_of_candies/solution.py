class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxval = max(candies)
        for v in candies:
            if v + extraCandies >= maxval:
                res.append(True)
            else:
                res.append(False)
        return res