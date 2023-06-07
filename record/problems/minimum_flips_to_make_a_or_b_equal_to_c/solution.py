class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            bit_a = a % 2
            bit_b = b % 2
            bit_c = c % 2
            if bit_c == 0:
                res += (bit_a + bit_b)  
            else:
                if bit_a == 0 and bit_b == 0:
                    res += 1 
            c = c >> 1 
            b = b >> 1
            a = a >> 1
        return res


     