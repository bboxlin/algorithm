class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 1
        buf = 0
        mul = 1
        for i in range( len(s)-1, -1, -1 ):
            num = int(s[i])
            if num > k: return -1
            if buf + num*mul <= k:
                buf += num*mul
                mul *= 10
            else:
                buf = num
                mul = 10
                ans += 1
        return ans

        