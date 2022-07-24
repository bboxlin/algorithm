class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        rowItems = collections.defaultdict(list)
        colItems = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                rowItems[i].append(grid[i][j])
                colItems[j].append(grid[i][j])
        
        ans = 0
        for rowidx, ritems in rowItems.items():
            for colidx, citems in colItems.items():
                if ritems == citems:
                    ans += 1        
        return ans
        