class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = []
        for ch in s.lower():
            if ch.isalpha() or ch.isdigit():
                words.append(ch)
        i, j = 0, len(words) - 1
        while i < j:
            if words[i] == words[j]:
                i += 1
                j -= 1
            else:
                return False 
        return True