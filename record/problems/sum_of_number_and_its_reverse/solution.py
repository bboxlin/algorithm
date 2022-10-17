class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
    
        for a in range(num//2,num+1):
            str_a = str(a)
            str_b = "".join(reversed(str_a))
            if int(str_a) + int(str_b) == num:
                return True
        return False