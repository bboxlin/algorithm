class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0:
            cur = carry
            if i >= 0: cur += ord(a[i]) - ord('0')
            if j >= 0: cur += ord(b[j]) - ord('0')
            carry = cur // 2 
            res = str(cur % 2) + res
            i -= 1
            j -= 1
        if carry != 0:
            res = str(carry) + res
        return res
