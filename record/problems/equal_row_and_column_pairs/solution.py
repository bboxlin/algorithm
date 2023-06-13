class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        freq = defaultdict(int)
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            freq[tuple(grid[i])] += 1

        for j in range(cols):
            curcol = []
            for i in range(rows):
                curcol.append(grid[i][j])
            res += freq[tuple(curcol)]
        return res
