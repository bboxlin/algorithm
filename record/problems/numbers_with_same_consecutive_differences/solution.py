class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = deque([1,2,3,4,5,6,7,8,9])
        n -= 1
        while n > 0:
            levelLen = len(q)
            for _ in range(levelLen):
                curnum = q.popleft()
                up = (curnum % 10) + k
                down = (curnum % 10) - k
                if 0 <= up <= 9:
                    newnum = curnum * 10 + up
                    q.append(newnum)
                    
                # make sure that k is not 0 otherwise up and down will be same, produce duplicates
                if k!=0 and 0 <= down <= 9:
                    newnum = curnum * 10 + down
                    q.append(newnum)
            n -= 1
        return list(q)