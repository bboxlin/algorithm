class Solution:
    def longestCycle(self, edges: List[int]) -> int:  

        def getCycleLen(node):
            d = 0
            pos = {}
            while node != -1 and node not in visited:
                pos[node] = d
                visited.add(node)
                node = edges[node]
                d += 1
            if d and node in pos.keys():
                return d - pos[node]
            return -1
        
        # visited on here instead of inside the getCycleLen
        # because if the path has cycle then len will be recorded
        # potentially bigger cycle only happens with additional unkown node
        
        # also if a path no cycle, we dont have to go again
        visited = set() 
        n = len(edges)
        ans = -1
        for node in range(n):
            cycle_len = getCycleLen(node)
            ans = max(ans, cycle_len)
        return ans
        