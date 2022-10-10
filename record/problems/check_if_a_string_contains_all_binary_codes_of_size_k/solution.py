class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        seen = set()
        # 2^k distincts
        for i in range(n):
            if i + k <= n:
                sub = s[i: i+k]
  
                seen.add(sub)
 
        if len(seen) == 2**k:
            return True
        return False
            