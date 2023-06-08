class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        4   3  2  -1
        3   2  1  -1
        1   1  -1 -2
        -1 -1 -2  -3
        """
        res = 0
        rows = len(grid)
        i = 0 
        j = len(grid[0]) - 1
        while i < rows and j >= 0:
            if grid[i][j] < 0:
                res += rows - i
                j -= 1
            else:
                i += 1
        return res

            
