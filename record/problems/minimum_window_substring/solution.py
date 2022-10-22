class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # O(t+s) time
        if len(s) < len(t): return ""
        tcounter = Counter(t)
        windowcnt = defaultdict(int)
        have, need = 0, len(tcounter)
        minlen = L = R = math.inf 
        l = 0
        
        for r in range(len(s)):
            windowcnt[s[r]] += 1
            if s[r] in tcounter and windowcnt[s[r]] == tcounter[s[r]]:
                have += 1
            while have == need:
                curlen = r - l + 1
                if curlen < minlen:
                    minlen = curlen
                    L = l
                    R = r
                windowcnt[s[l]] -= 1
                if s[l] in tcounter and windowcnt[s[l]] < tcounter[s[l]]:
                    have -= 1
                l+=1
        return s[L:R+1] if L != math.inf and R != math.inf else ""
        
             
                
