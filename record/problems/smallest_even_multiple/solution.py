class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for val in range(n, 2*n+1):
            if val % 2 == 0 and val % n == 0:
                return val
            