class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted) 
        visited = set()
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def search(node):
            if node not in graph.keys() or node in visited or node in restricted:
                return 
            
            self.ans += 1
            visited.add(node)
            
            for r_node in graph[node]:
                search(r_node)
            
            visited.remove(node)
            
        self.ans = 0
        search(0)
        return self.ans