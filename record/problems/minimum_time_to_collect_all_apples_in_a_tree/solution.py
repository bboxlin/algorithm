class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(cur, par):
            time = 0
            for child in graph[cur]:
                if child == par: continue
                childTime = dfs(child,cur)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            return time
        return dfs(0, -1)
                
