class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        def dfs(curnode, destination, visited):        
            if curnode == destination:
                return True
            if curnode in visited:
                return False
            visited.add(curnode)
            for node in graph[curnode]:
                if dfs(node, destination, visited):
                    return True
            return False         
        return dfs(source, destination, set() )