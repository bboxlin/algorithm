class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        match = [0] * 26
        for ch in s1:
            match[ord(ch)-ord('a')] += 1
        
        # window setup
        window  = [0] * 26
        winsize = len(s1)
        for i in range(winsize):
            window[ord(s2[i]) - ord('a')] += 1
        
        if window == match: return True

        # window sliding 
        for i in range(winsize, len(s2)):
            window[ord(s2[i]) - ord('a')] += 1 
            window[ord(s2[i-winsize]) - ord('a')] -= 1
            if window == match:
                return True 
        return False


    
        
        
