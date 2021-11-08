class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def length(coordinate):
            return abs(coordinate[0]*coordinate[0]) + abs(coordinate[1]*coordinate[1])
        
        memo = []
        for point in points:
            distance = length(point)
            memo.append((distance, point))
        #[(distanct, [point]) ... ]
         
        memo.sort(key = lambda x:x[0])
        res = []
        
        for i in range(k):
            res.append(memo[i][1])
        return res
            

                

    