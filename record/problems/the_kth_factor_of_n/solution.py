class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        """
        
        1, 2, 3, 4, 6, 12 
        
        first loop:   1,    2,   3
        second loop, n/3, n/2, n/1
                      4    6    12
        """
        
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                k -= 1
                if k == 0: return i
        
        for i in range(int(n**0.5), 0, -1):
            if i*i == n: continue   # i has been visited in previous loop
            if n % i == 0:
                k -= 1
                if k == 0: return n // i
        return -1
            
            
        
        
         