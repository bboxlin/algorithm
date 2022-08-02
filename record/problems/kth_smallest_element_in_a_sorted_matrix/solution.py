import heapq
class Solution:
    
    # Binary Search 
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countSmallerOrEqual(m):
            i, j = n-1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= m:
                    num += (i + 1)
                    j += 1
                else:
                    i -= 1
            return num
        
        # ower+(upper-lower)/2 和 upper-(upper-lower)/2 
        # 0 + (9-0)/2 = 0 + 4 = 4 靠左
        # 9 - (9-0)/2 = 9 - 4 = 5 靠右
        # O(log （Max - Min) * O(n)
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = lo + (hi-lo) // 2
            if countSmallerOrEqual(mid) < k:
                lo = mid+1
            else:
                hi = mid 
        return lo
        

    # Heap Solution
    # def kthSmallestHeap(self, matrix: List[List[int]], k: int) -> int:
    #     heap = [(row[0], i, 0) for i, row in enumerate(matrix)] #O(n)
    #     heapq.heapify(heap)  #O(n)
    #     ret = 0
    #     for _ in range(k):   # k*logN
    #         ret, i, j = heapq.heappop(heap)
    #         if j+1 < len(matrix[0]):
    #             heapq.heappush(heap, (matrix[i][j+1], i, j+1))
    #     return ret
            