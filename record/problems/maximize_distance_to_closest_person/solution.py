class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        maxempty = 0
        empty = 0
        n = len(seats)
        
        # empty seats in between 
        for i in range(n):
            if seats[i] == 0:
                empty += 1
            else:
                maxempty = max(maxempty, empty)
                empty = 0
        ans = (maxempty + 1) // 2 
        
        i = 0
        while i < n and seats[i] == 0:
            i += 1
        ans = max(i, ans)
        
        j = n-1
        while j >= 0 and seats[j] == 0:
            j -= 1
        ans = max(n-1-j, ans)
        
        return ans
        
        
        
        
    # 1 0 0 0 0 1 
                