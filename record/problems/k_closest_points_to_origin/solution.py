import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []   
        for x, y in points:
            tup = (x*x+y*y, [x, y])
            heapq.heappush(min_heap, tup)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res
        
                

            
        
        
            

                

    