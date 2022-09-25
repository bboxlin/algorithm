class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = [] 
        n = len(arr)
        minDiff = math.inf
        for i in range(1, n):
            minDiff = min(minDiff, abs(arr[i]-arr[i-1]))
        
        for i in range(1, n):
            curDiff = abs(arr[i]-arr[i-1])
            if curDiff == minDiff:
                ans.append([arr[i-1], arr[i]])
        return ans