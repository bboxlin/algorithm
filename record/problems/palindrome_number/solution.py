class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False 
        if x == 0: return True 
        
        digits = []
        while x:
            d = x % 10
            x = x // 10
            digits.append(d)
        
        l, r = 0, len(digits) - 1
        while l < r:
            if digits[l] != digits[r]:
                return False 
            l += 1
            r -= 1
        return True
        