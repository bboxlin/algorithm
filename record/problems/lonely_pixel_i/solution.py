class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = len(picture)
        cols = len(picture[0])
        rowB = defaultdict(int)
        colB = defaultdict(int)
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B':
                    rowB[i] += 1
                    colB[j] += 1
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if picture[i][j] == 'B' and rowB[i] == 1 and colB[j] == 1:
                    ans += 1
        return ans
        
        
        