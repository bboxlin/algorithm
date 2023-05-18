class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def mark(i):
            if visited[i]: return 
            visited[i] = True 
            for nxt in graph[i]:
                mark(nxt)
        visited = [False] * n
        graph = defaultdict(list)
        for x, y in edges: graph[x].append(y)
        for x, y in edges:
            mark(y)
        return [i for i in range(n) if visited[i] == False]

