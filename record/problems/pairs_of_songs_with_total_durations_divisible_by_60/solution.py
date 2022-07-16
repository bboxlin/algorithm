class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:    
        lookup = collections.defaultdict(int)
        cnt = 0 
        for n in time:
            if n % 60 == 0:
                cnt += lookup[0]
            else:
                rem = 60 - n % 60
                cnt += lookup[rem]
            lookup[n%60] += 1
        return cnt
                    