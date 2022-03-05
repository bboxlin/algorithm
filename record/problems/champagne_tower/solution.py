class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # [0] 
        # [0 0]
        # .........
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        
        for r in range(query_row):
            for c in range(r+1):
                portion = float((A[r][c] - 1) / 2)
                if portion > 0:
                    A[r+1][c] += portion
                    A[r+1][c+1] += portion
        return min(1, A[query_row][query_glass])