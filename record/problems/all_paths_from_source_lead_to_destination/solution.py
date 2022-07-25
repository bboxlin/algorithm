class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Source lead to Destination 定義
        
        1. 中途不能出現環
        2. Destination不能有outgoing edges

        """
        def isAllReachable(node):
            
            if len(graph[node]) == 0: # Destination不能有outgoing edges
                if node == destination:
                    return True
                return False 
            
            if node in visited:
                return False
            
            visited.add(node)
            for reachNode in graph[node]:
                if isAllReachable(reachNode) == False:
                    return False 
            visited.remove(node)
            return True
            
        visited = set()
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            
        return isAllReachable(source)
            
        