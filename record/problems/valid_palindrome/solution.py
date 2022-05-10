class Solution:
    def isPalindrome(self, s: str) -> bool:
        strlst = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        i, j = 0, len(strlst)-1
        while i <= j:
            if strlst[i] != strlst[j]:
                return False
            i += 1
            j -= 1
        return True