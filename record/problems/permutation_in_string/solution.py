class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2: return False 
        
        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c)-ord('a')] += 1
        
        s2_freq = [0] * 26
        for i in range(len_s1):
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        if s1_freq == s2_freq: return True 
        
        for r in range(len_s1, len_s2):
            addchar = s2[r] # r =2
            removechar = s2[r-len_s1] # 2-2= 0
            
            s2_freq[ord(addchar) - ord('a')] += 1
            s2_freq[ord(removechar) - ord('a')] -= 1
            
            if s1_freq == s2_freq: return True
            
        return False
    
            
        
        
        
        