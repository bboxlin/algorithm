class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        n = min( len(str1), len(str2) )
        for i in range(n):
            p1 = s1 = str1[:i+1]
            p2 = s2 = str2[:i+1]
            if s1 != s2: continue 
            while len(p1) < len(str1):
                p1 += s1
            while len(p2) < len(str2):
                p2 += s2 
            if p1 != str1 or p2 != str2: continue 
            if len(s1) > len(ans):
                ans = s1
        return ans
