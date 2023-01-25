class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        d1 = [-1]* n
        d2 = [-1]* n
        
        def markDistance(node, dis):
            d = 0 
            # node != -1 handles reach end 
            # dis[node] == -1 handles not fall into cycles
            while node != -1 and dis[node] == -1:
                dis[node] = d
                d += 1
                node = edges[node]
   
        markDistance(node1, d1)
        markDistance(node2, d2)
        
        mindis = float('inf')
        ansnode = -1
        for i in range(n-1, -1, -1):
            if d1[i] != -1 and d2[i] != -1:
                if max(d1[i], d2[i]) <= mindis:
                    ansnode = i
                    mindis = max(d1[i], d2[i])           
        return ansnode

                