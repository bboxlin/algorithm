class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = len(s)
        chars = set(s)
        for i in range(n):
            curchar = s[i]
            d = distance[ord(curchar) - ord('a')]
            if i + d + 1 < n and s[i+d+1] == curchar and curchar in chars:
                chars.remove(curchar)
        return len(chars) == 0
            