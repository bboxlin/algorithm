class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        print(graph)
        def dfs(city):
            visited.add(city)
            p = 0
            f = 0
            for nxtcity in graph[city]:
                if nxtcity in visited: continue
                dp, df = dfs(nxtcity)
                p += dp 
                f += df
                print('in', city)
            
            print('out', city)
            # when we at capital return (p,f)
            if city == 0:
                return (p,f)
 
            # else propagate up
            p += 1
            f += ceil(p/seats)
            
            return (p,f)
        visited = set()
        return dfs(0)[1]