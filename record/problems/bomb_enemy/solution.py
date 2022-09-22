class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        enemyLeftCount = defaultdict(int)
        enemyUpCount = defaultdict(int)
        
        # traverse from left upper conner to right lower conner
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'E':
                    enemyLeftCount[(i,j)] = enemyLeftCount[(i,j-1)] + 1 if j > 0 else 1 
                    enemyUpCount[(i,j)] = enemyUpCount[(i-1,j)] + 1 if i > 0 else 1 
                elif grid[i][j] == 'W':
                    enemyLeftCount[(i,j)] = 0
                    enemyUpCount[(i,j)] = 0
                else:
                    enemyLeftCount[(i,j)] = enemyLeftCount[(i,j-1)] if j > 0 else 0
                    enemyUpCount[(i,j)] = enemyUpCount[(i-1,j)] if i > 0 else 0
        
        enemyRightCount = defaultdict(int)
        enemyBottomCount = defaultdict(int)
        
        # traverse from right lower conner to left upper conner
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if grid[i][j] == 'E':
                    enemyRightCount[(i,j)] = enemyRightCount[(i,j+1)] + 1 if j < cols - 1 else 1 
                    enemyBottomCount[(i,j)] = enemyBottomCount[(i+1,j)] + 1 if i < rows - 1 else 1 
                elif grid[i][j] == 'W':
                    enemyRightCount[(i,j)] = 0
                    enemyBottomCount[(i,j)] = 0
                else:
                    enemyRightCount[(i,j)] = enemyRightCount[(i,j+1)] if j < cols - 1 else 0
                    enemyBottomCount[(i,j)] = enemyBottomCount[(i+1,j)] if i < rows - 1 else 0
        print(enemyRightCount)
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    curkill = enemyLeftCount[(i,j)] + enemyRightCount[(i,j)] + enemyUpCount[(i,j)]  + enemyBottomCount[(i,j)]
                    ans = max(curkill, ans)
        return ans
                   
                    