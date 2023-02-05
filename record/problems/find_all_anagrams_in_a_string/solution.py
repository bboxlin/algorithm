class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcnt = [0]*26
        for c in p:
            pcnt[ord(c) - ord('a')] += 1
        
        window = [0]*26
        res = []
        for i, c in enumerate(s):
            if i < len(p):
                window[ord(c) - ord('a')] += 1
            else:
                window[ord(c) - ord('a')] += 1
                window[ ord(s[i-len(p)]) - ord('a')] -=1 
            if window == pcnt:
                res.append(i-len(p)+1)
        return res


