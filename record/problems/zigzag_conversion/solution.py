class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        arr = [ [] for _ in range(numRows)]
        r = 0 
        d = 1
        for c in s:
            arr[r].append(c)
            r += d
            if r == numRows-1 or r == 0:
                d *= -1
        ans = "" 
        for sublist in arr:
            ans += "".join(sublist)
        return ans