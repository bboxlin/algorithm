class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding window, where the frequency in a window maintained in a freqTable
        
        """
        freqTable = defaultdict(int)
        maxcnt = 0
        ans = 0 
        l = 0 
        for r, ch in enumerate(s):
            freqTable[ch] += 1
            maxcnt = max(maxcnt, freqTable[ch])
            #总长度 - 最大频 = 可调整字符
            while r-l+1 - maxcnt > k:
                freqTable[s[l]] -= 1
                l+=1
            ans = max(ans, r-l+1)
        return ans
            