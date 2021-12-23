class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
                
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
                return -1
            return 0
                    
        root = [i for i in range(n)]
        rank = [1]*n
        for t,x,y in sorted(logs):
            n += union(x,y)
            if n == 1:
                return t
            
        return -1
            