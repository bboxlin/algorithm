class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
        graph = {crs:[] for crs in range(numCourses)}
        for crs, prep in prerequisites:
            graph[crs].append(prep)
        
        visited = set()
        courseTook = []
        cycle = set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            
            for prep in graph[crs]:
                if dfs(prep) == False:
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            courseTook.append(crs)
            return True
            
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return courseTook
        
                