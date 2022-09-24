class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        q = deque([(0,0,0)])
        visited = set()
        move = 0
        while q:
            levelsize = len(q)
            for _ in range(levelsize):
                thex, they, curmove = q.popleft()
                
                if thex == x and they == y:
                    return curmove
                
                for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1), (-1,-2), (-2,-1)]:
                    curx, cury = thex+dx, they+dy
                    if (curx,cury) not in visited and -1 <= curx <= x+2 and -1 <= cury <= y+2:
                        visited.add((curx, cury))
                        q.append((curx,cury, curmove+1))
                move += 1
        return -1
                
                    
                  
                 
                
                 
                
                        
                    