class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        res = 0
        for amount, start, end in trips:
            while heap and heap[0][0] <= start:
                last_end, prevamount = heappop(heap)
                res -= prevamount
            heappush(heap, (end, amount)) 
            res += amount
            if res > capacity:
                return False
        return True