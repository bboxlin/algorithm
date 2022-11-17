class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        oricolor = image[sr][sc]
        filled = set()
        def go(i, j):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
                return
            if image[i][j] != oricolor:
                return
            if (i,j) in filled:
                return
            filled.add((i,j))
            image[i][j] = color
            for di, dj in [(1,0), (-1, 0), (0,1), (0,-1)]:
                go(i+di,j+dj)
        go(sr,sc)
        return image