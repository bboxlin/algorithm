class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        return " ".join(reversed(lst))