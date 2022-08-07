class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        x = [ord(i)-97 for i in s]
        res = [0]*26
        for i in x:
            cur = 1
            for j in range(26):
                if abs(i-j) <= k:
                    cur = max(cur, res[j] + 1)
            res[i] = max(res[i], cur)
        return max(res)