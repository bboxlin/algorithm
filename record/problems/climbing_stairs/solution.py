class Solution:
    def climbStairs(self, n: int) -> int:
        p, q = 1, 2 
        if n == 1: return p
        elif n == 2: return q
        for i in range(2,n):
            temp = q
            q = p + q
            p = temp
        return q
            
            
            