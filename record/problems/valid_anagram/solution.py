class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(nlogn) time O(n) space
        # sCH = [ c for c in s]
        # tCH = [ c for c in t]
        # sCH.sort() 
        # tCH.sort()
        # return sCH == tCH
        
        # 26 letters 
        # ascii 编码
        # a --> 97
        # b --> 98 
        # O(n) time  O(n) space
        sFreq = [0] * 26 
        tFreq = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            sFreq[idx] += 1
        for c in t:
            idx = ord(c) - ord('a')
            tFreq[idx] += 1
        return sFreq == tFreq