class Solution:
    def getFood(self, grid: List[List[str]]) -> int: 
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '*':
                    q.append((i,j))
        cnt = 0
        while q:
            len_level = len(q)
            for _ in range(len_level):
                pos_i, pos_j = q.popleft()
                if grid[pos_i][pos_j] == '#':
                    print(cnt)
                    return cnt
                grid[pos_i][pos_j] = 'X'
                for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
                    cur_i = pos_i + i 
                    cur_j = pos_j + j 
                    if 0 <= cur_i < ROWS and 0 <= cur_j < COLS and grid[cur_i][cur_j] !='X':
                        q.append((cur_i, cur_j))
                        if grid[cur_i][cur_j] != '#':
                            grid[cur_i][cur_j] = 'X' # mark visited
            cnt += 1
        return -1
                    
            
             