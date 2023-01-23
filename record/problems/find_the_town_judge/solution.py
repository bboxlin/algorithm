class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # got trust + 1, trust other -1
        t = [0] * (n+1) 
        for x, y in trust:
            t[x] -= 1
            t[y] += 1
        for i in range(1, n+1):
            if t[i] == n-1: return i 
        return -1