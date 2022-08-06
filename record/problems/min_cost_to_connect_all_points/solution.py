class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # time: n^2 logn 
        # space n^2
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        minheap = [(0,0)] # (cost, start point idx)
        visited = set()
        ans = 0
        while len(visited) < n:
            cost, vtx = heapq.heappop(minheap)
            if vtx in visited: continue 
            ans += cost
            visited.add(vtx)
            for j in range(n):
                if j != vtx and j not in visited:
                    costs2 = manhattan(points[vtx], points[j])
                    heapq.heappush(minheap, (costs2, j))
        return ans
    