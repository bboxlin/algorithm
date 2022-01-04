import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-1*n for n in nums]
        heapq.heapify(maxheap)
        res = None
        while k > 0:
            res = heapq.heappop(maxheap) * (-1)
            k -= 1
        return res
        
            
        