class Solution:
    def minimizeXor(self, a: int, b: int) -> int:
        setBits = bin(b).count('1')
        ans = 0
        for i in range(30, -1, -1):
            mask = (1 << i)
            s = (a & mask)
            if (s and setBits > 0):
                ans |= (1 << i)
                setBits -= 1
            i = 0
        while(setBits > 0):
            mask = (1 << i)
            if (ans & mask) == 0:
                ans |= (1 << i)
                setBits -= 1
            i += 1
        return ans