class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def counter(n):
            if n <= 1: return 1
            if n in memo: return memo[n]
            else:
                count = 0
                for i in range(0, n):#(0,n-1)
                    count += counter(i) * counter(n-1-i)  #(0,n-1) (1,n-2) (2,n-3) subtrees 
                memo[n] = count
                return count      
        return counter(n)