class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False
         
        cntS1, cntS2 = [0]*26, [0]*26
        for i in range(len1):
            cntS1[ord(s1[i]) - ord('a')] += 1
            cntS2[ord(s2[i]) - ord('a')] += 1
        if cntS1 == cntS2: return True
        
        for i in range(len1, len2):
            cntS2[ord(s2[i]) - ord('a')] += 1
            cntS2[ord(s2[i-len1]) - ord('a')] -= 1
            if cntS1 == cntS2: return True
        return False
        
            
                
            
            
            