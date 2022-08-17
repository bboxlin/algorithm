class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        values[i] + values[j] + i - j =  (values[i] + i) + (values[j] - j)
        
        max (values[i] + i) + (values[j] - j)
        """
        n = len(values)
        maxi = values[0]
        ans = 0
        for i in range(1, n):
            ans = max(ans, maxi + values[i] - i)
            maxi = max(maxi, values[i] + i)
        return ans
            
        