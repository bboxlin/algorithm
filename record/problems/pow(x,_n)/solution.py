class Solution:
    def myPow(self, x: float, n: int) -> float:
        
#         def power (n):
#             if not n:
#                 return 1
#             if n < 0:
#                 return 1/power(-n)
#             if n % 2:
#                 return x*power(n-1)
#             return power(x*)
        
#         if n < 0:
#             return power(1/x, abs(n))
#         elif n == 0:
#             return float(1)
#         else:
#             return power(x, n)
        
        
        if n < 0:
            x, n = 1/x, -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x = x*x
            n >>= 1
        return res