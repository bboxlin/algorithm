class Circle:
    def __init__(self, x,y,r):
        self.x = x
        self.y = y 
        self.r = r

    def isWithInMyDetonate(self, circle):
        dpow2 = (self.x - circle.x)**2  + (self.y - circle.y)**2
        return self.r**2 >= dpow2

"""
从某个圆开始
- graph[cirle1] = [...] with n = 5
- 则[...] with n = 5 的circle都没被visited, 则res += 5

- 注意：这题不是算最长深度.. 而是最长总数。

"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(cir, visited):
            visited.add(cir)
            for nxtcir in graph[cir]:
                if nxtcir not in visited:
                    dfs(nxtcir, visited)

        # Build Graph
        circleList = [Circle(x,y,r) for x,y,r in bombs]
        graph = defaultdict(list)
        n = len(circleList)
        for i in range(n):
            curCircle = circleList[i]
            for j in range(n):
                if j == i: continue 
                nxtCircle = circleList[j]
                if curCircle.isWithInMyDetonate(nxtCircle):
                    graph[curCircle].append(nxtCircle)

        res = 0
        for i in range(n):
            visited = set()
            dfs(circleList[i], visited)
            res = max(res, len(visited))
        return res