class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        """
                        1317
        (1, 317)  (13, 17)  (131, 7)  (1317) --> sub prolems
    ...........  ......... ..........  ..........
        """
        @cache
        def f(i):
            if i == n: return 1
            if s[i] == '0': return 0
            res = 0
            for j in range(i+1, n+1):
                curnum = int(s[i:j]) 
                # no combination with curnum will work..
                if curnum > k: break
                res += f(j) % mod
            return res
        n = len(s)
        mod = 10**9 + 7
        return f(0) % mod

