import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        minHeap = []
        N = len(matrix)
        for r in range(min(k,N)):
            # tuple (item, row, col)
            tup = (matrix[r][0], r, 0)
            minHeap.append(tup)
        
        heapq.heapify(minHeap)
        
        res = None
        for i in range(k):
            
            val, r, c = heapq.heappop(minHeap)
            res = val
            
            if c < N-1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            
        return res
            