import collections
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        return max(len(graph[a]) + len(graph[b]) - (1 if b in graph[a] else 0) for a in range(n) for b in range(a + 1, n))

            
        
            