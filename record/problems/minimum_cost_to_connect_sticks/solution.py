import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) < 2: return 0
        heapq.heapify(sticks)
        total = 0
        while len(sticks) > 1:
            x =  heapq.heappop(sticks)
            y =  heapq.heappop(sticks)
            total += (x+y)
            heapq.heappush(sticks, x+y)

        return total
        