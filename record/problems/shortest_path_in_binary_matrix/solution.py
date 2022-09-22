class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] != 0:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        
        direc = [(-1,-1), (1, 1), (1,-1), (-1,1), (0, 1), (1, 0), (0, -1), (-1, 0)]
        
        visited = set()
        q = deque([(0,0,1)])
        visited.add((0,0))
        
        
        while q:
            i, j, d = q.popleft()      
            
            # since BFS first encounter is shortest!
            if i == rows - 1 and j == cols - 1:
                return d
            
            for di, dj in direc:
                if 0 <= i + di < rows and 0 <= j + dj < cols:
                    newi = i + di
                    newj = j + dj
                     
                    if grid[newi][newj] == 0 and (newi, newj) not in visited:                  
                        q.append((newi,newj,d+1)) 
                    
                    # mark current pos visited
                    visited.add((newi,newj))      
        return -1
  