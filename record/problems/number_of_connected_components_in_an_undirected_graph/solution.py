class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for dnode in graph[node]:
                if dnode not in visited:
                    dfs(dnode)

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        ans = 0
        for x in range(n):
            if x not in visited:
                dfs(x)
                ans += 1

        return ans
