class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        ans = [] 
        while intervals:
            left, right = heapq.heappop(intervals)
            if len(ans) == 0:
                ans.append([left,right])
            elif ans[-1][1] >= left:
                ans[-1][1] = max(right, ans[-1][1])
            else:
                ans.append([left,right])
        return ans
                