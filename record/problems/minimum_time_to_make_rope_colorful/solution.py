class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # greedy, always remove with less time
        # suppose there are k consecutive color, we will have to remove k-1 ballon
        # to do that, we can keep the max time consuming ballon
        n = len(colors)
        i = 0 
        ans = 0 
        while i < n:
            j = i+1
            curCosts = neededTime[i]
            curMaxCost = neededTime[i]
            while j < n and colors[j] == colors[j-1]:
                curCosts += neededTime[j]
                curMaxCost = max(curMaxCost, neededTime[j])
                j += 1
            ans += curCosts-curMaxCost
            i = j
        return ans
            
                
            
            
                