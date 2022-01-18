class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i] 
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in dic and dfs(j):
                    #cache[j] = True
                    return True
            cache[i] = False
            return False
        cache = {}
        dic = set(wordDict)
        return dfs(0)

            
        
            