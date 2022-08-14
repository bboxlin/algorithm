class Solution:
    def edgeScore(self, edges: List[int]) -> int:   
        n = len(edges)
        scores = [0] * n
        for source, destination in enumerate(edges):
            scores[destination] += source
        
        maxscore = 0 
        ans = -1
        for idx, score in enumerate(scores):
            if score > maxscore:
                maxscore = score
                ans = idx
        return ans