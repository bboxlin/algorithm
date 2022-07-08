class Solution:
    def minimumBuckets(self, street: str) -> int:
        # "HB.H"
        streetList = list(street)
        n = len(streetList)
        cnt = 0
        for i in range(n):
            if streetList[i] == 'H':
                if (i-1 >= 0 and streetList[i-1] == 'B'):
                    continue 
                elif (i+1 < n and streetList[i+1] == '.'):
                    streetList[i+1] = 'B'
                    cnt += 1
                elif (i-1 >= 0 and streetList[i-1] == '.'):
                    streetList[i-1] = 'B'
                    cnt += 1
                else:
                    return -1
        return cnt
                    
            
                