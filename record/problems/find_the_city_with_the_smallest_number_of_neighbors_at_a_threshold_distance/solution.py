class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        # graph init
        graphMatrix = [[inf]*n for _ in range(n)]
        for x,y, w in edges:
            graphMatrix[x][y] = w
            graphMatrix[y][x] = w
            
        for i in range(n):
            graphMatrix[i][i] = 0
        
        # Floyd Warshall Algorithm 
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graphMatrix[i][j] = min(graphMatrix[i][j], graphMatrix[k][j] + graphMatrix[i][k])
        
        cityCnt = inf
        cityNum = -1
        for x in range(n):
            reachCityCnt = 0
            for y in range(n):
                if graphMatrix[x][y] <= distanceThreshold:
                    reachCityCnt += 1
            if reachCityCnt <= cityCnt:
                cityCnt = reachCityCnt
                cityNum = x
        return cityNum
                    
        
            