class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for j in range(n+1):
            for i in range(j):
                # if word ending i is true, and now i:j is in wordDict, then at j is True
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    break
        print(dp)
        return dp[n]
            
        
            