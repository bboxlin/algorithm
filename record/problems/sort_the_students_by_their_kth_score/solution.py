class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        m, n = len(score), len(score[0])
        for i in range(m):
            temp.append([score[i][k], score[i]])
        temp.sort(reverse=True)
        return [ arr for score, arr in temp]
        