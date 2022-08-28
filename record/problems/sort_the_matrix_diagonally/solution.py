class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        idxmap = defaultdict(list)
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(m):
                idxmap[i-j].append(mat[i][j]) 
        
         
        for k, v in idxmap.items():
            heapq.heapify(v)
            
        ans = [ [0 for _ in range(m) ] for _ in range(n) ] 
        
        for i in range(n):
            for j in range(m):
                minheap = idxmap[i-j] 
                v = heapq.heappop(minheap)
                ans[i][j] = v
                
        return ans
            