import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1*stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)
            if y-x == 0: continue
            heapq.heappush(max_heap, y-x)
        if not max_heap: return 0
        return heapq.heappop(max_heap)*(-1)