class Solution:
    """
    actually DP about sequence sum => 2 loops 
    """
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        tuplist = [(ages[i], scores[i]) for i in range(n)]
        tuplist.sort() 

        # cache max scores at i
        dp = [0] * n 
        for i in range(n):
            age, score = tuplist[i]
            dp[i] = score
            for j in range(i):
                page, pscore = tuplist[j]
                # when no conflict try to add j into team.
                if pscore <= score:
                    dp[i] = max(dp[i], dp[j] + score)        
        return max(dp)
