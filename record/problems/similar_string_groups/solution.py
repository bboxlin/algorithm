class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s1, s2):
            d = 0
            for c1,c2 in zip(s1,s2):
                if c1 != c2:
                    d += 1
            return d <= 2
        
        # dfs will mark all similar string of given s..
        def dfs(s1):
            for i in range(n):
                s2 = strs[i]
                if i in visitedIdx:
                    continue
                if isSimilar(s1, s2):
                    visitedIdx.add(i)
                    dfs(s2)
                
        visitedIdx = set()
        res = 0
        n = len(strs)
        for i in range(n):
            if i in visitedIdx:
                continue
            dfs(strs[i])
            res += 1
        return res