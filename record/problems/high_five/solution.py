class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student2scores = collections.defaultdict(list)
        for studentId, studentScore in items:
            student2scores[studentId].append(studentScore)
        
        ans = []
        for studentId, studentScores in student2scores.items():
            heapq.heapify(studentScores)
            while len(studentScores) > 5:
                heapq.heappop(studentScores)
            avgScore = sum(studentScores) // 5
            ans.append([studentId,avgScore])
        
        return sorted(ans, key=lambda x: x[0])