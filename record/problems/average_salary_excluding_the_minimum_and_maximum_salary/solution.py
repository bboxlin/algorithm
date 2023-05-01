class Solution:
    def average(self, salary: List[int]) -> float:
        minv = min(salary)
        maxv = max(salary)
        sumv = sum(salary)
        n = len(salary)
        return float((sumv - minv - maxv) / (n - 2))