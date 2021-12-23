class UandF:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        self.count = size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:   
        n = len(isConnected)
        if n == 0: return 0
        uf = UandF(n)
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        print(uf.root)
        return uf.count

                    