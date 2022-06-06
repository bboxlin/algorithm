import collections
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        print(rows, cols)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1
        return ans
        