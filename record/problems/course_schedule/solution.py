class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {c:[] for c in range(numCourses)}
        for c, p in prerequisites:
            graph[c].append(p)
        
        cycle = set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            
            if graph[crs] == []:
                return True
            
            cycle.add(crs)
            for prep in graph[crs]:
                if dfs(prep) == False:
                    return False
            cycle.remove(crs)
            graph[crs] = []
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True