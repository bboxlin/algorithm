class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        print(matrix)
        val, maxx = 1, n*n
        t, b, l, r = 0, n-1, 0, n-1
        while val <= maxx:
            for i in range(l, r+1):
                matrix[t][i] = val
                val += 1
            t += 1
            for i in range(t, b+1):
                matrix[i][r] = val 
                val += 1
            r -= 1
            for i in range(r, l-1, -1):
                matrix[b][i] = val 
                val += 1
            b -= 1
            for i in range(b, t-1, -1):
                matrix[i][l] = val
                val += 1
            l += 1
        return matrix