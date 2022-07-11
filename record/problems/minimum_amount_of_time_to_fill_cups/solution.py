import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        maxheap = [ -1*n for n in amount]
        cnt = 0
        heapq.heapify(maxheap)
        while maxheap:
            firstmax = heapq.heappop(maxheap)
            secondmax = heapq.heappop(maxheap)
            if firstmax == 0: break
            firstmax += 1
            secondmax += 1
            heapq.heappush(maxheap, firstmax)
            heapq.heappush(maxheap, secondmax)
            cnt += 1
        return cnt