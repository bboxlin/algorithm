class Solution:
    def minInsertions(self, s: str) -> int:
        """
        mbadm
         i j
        either:
        1. insert d at i
        2. insert b at j
        f(i, j) = min insert needed for s[i...j] to be panlindrom
        f(i, j) = f(i+1, j-1) if s[i] == s[j]
        f(i, j) = min{ f(i+1, j), f(i, j-1) } + 1
        """
        @cache
        def f(i,j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return f(i+1,j-1)
            else:
                return min( f(i+1, j), f(i, j-1)) + 1
        return f(0, len(s)-1)