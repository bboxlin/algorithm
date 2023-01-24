class Solution:
    def snakesAndLadders(self, board):
        def pos(num):
            r = (num - 1) // n
            c = (num - 1) % n 
            if r % 2 != 0:
                c = n - 1 - c
            return n-r-1,c
 
        n = len(board)
        q = collections.deque()
        q.append([1,0])
        visited = set() 
        while q:
            num, cnt = q.popleft()
            for i in range(1,7):
                nextnum = num + i 
                r,c = pos(nextnum)
                if board[r][c] != -1:
                    nextnum = board[r][c]
                if nextnum == n * n:
                    return cnt + 1
                if nextnum not in visited:
                    visited.add(nextnum)
                    q.append([nextnum, cnt+1])
        return -1


                