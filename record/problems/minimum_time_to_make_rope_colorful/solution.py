class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        i  = 0 
        while i < len(colors):
            groupSum, maxSum = 0, 0
            j = i
            while j < len(colors) and colors[j] == colors[i]:
                groupSum += neededTime[j]
                maxSum = max(maxSum, neededTime[j])
                j += 1
            ans += groupSum - maxSum
            i = j
        return ans