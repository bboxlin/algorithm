import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_soldiers = {}
        for row, sublist in enumerate(mat):
            for val in sublist:
                if not row in row_soldiers:
                    row_soldiers[row] = 0
                row_soldiers[row] += val
        min_heap = [(soldiers, row) for row, soldiers in row_soldiers.items()]
        heapq.heapify(min_heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res