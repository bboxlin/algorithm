import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            else:
                freq[n] += 1
        max_heap = [(-fre, n) for n, fre in freq.items()]
        heapq.heapify(max_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res
            
                
            
            