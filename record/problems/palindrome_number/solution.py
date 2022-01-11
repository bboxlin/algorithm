class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        reverse, xvalue = 0, x
        while x:
            rem = x % 10
            reverse = reverse*10 + rem
            x = x//10
        return reverse == xvalue