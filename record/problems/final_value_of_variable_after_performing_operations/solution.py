class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0
        for s in operations:
            if s[1] == '+':
                total += 1
            else:
                total -= 1
        return total