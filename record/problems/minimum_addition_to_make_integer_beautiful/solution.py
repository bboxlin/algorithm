class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        def getsum(val):
            nsum = 0
            while val:
                nsum += val%10
                val = val // 10
            return nsum
        
        # if n = xy > target
        # then zz > target for any z>x or z>y
        vals, tens = n, 1
        while getsum(vals) > target:
            vals = vals // 10 + 1
            tens = tens * 10
        return vals*tens-n
        
        
        