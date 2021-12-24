class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
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
        
        n = len(s)
        root = [i for i in range(n)]
        rank = [1]*n
        res, m = [], defaultdict(list)
        for x,y in pairs: 
            union(x,y)
        for i in range(len(s)): 
            m[find(i)].append(s[i])
        for comp_id in m.keys(): 
            m[comp_id].sort(reverse=True)
        for i in range(len(s)): 
            res.append(m[find(i)].pop())
        return ''.join(res)
        
        
        