class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
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
                    
        root = [i for i in range(n)]
        rank = [1]*n
        
        # union vertices
        for x, y in edges:
            union(x,y)
        
        # add all vertices find result to set
        distinct_root = set()
        for v_index in range(n):
            distinct_root.add(find(v_index)) 
            
        return len(distinct_root)