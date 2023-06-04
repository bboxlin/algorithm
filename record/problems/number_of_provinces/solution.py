class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(u):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)


        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()
        res = 0
        for city in range(n):
            if city not in visited:
                dfs(city)
                res += 1
        return res