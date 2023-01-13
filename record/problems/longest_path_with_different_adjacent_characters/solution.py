class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        @cache
        def dfs(node, prev):
            nonlocal ans
            maxpath = 1
            for nei in adjmap[node]:
                # loop or adjacent same
                if nei == prev or s[node] == s[nei]:
                    continue
                curpath = dfs(nei, node) + 1
                ans = max(ans, curpath)
                maxpath = max(curpath, maxpath)
            return maxpath

        adjmap = defaultdict(set)
        for child, par in enumerate(parent):
            if par == -1: continue
            adjmap[child].add(par)
            adjmap[par].add(child)

        ans = 1
        n = len(parent)
        for node in range(n):
            ans = max(ans, dfs(node, -1))
        return ans

