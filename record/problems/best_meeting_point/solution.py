class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        rowidx = []
        colidx = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowidx.append(i)
                    colidx.append(j)
        
        n = len(rowidx)
        rowidx.sort()
        colidx.sort()
        meetpoint = ((rowidx[n//2], colidx[n//2]))
        
        dis = 0 
        for i in range(n):
            xdf = abs(meetpoint[0] - rowidx[i])
            ydf = abs(meetpoint[1] - colidx[i])
            dis += xdf + ydf
        return dis