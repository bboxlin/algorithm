class Solution:
    """
    every number is 2*x+3*y except 1
    """
    def minimumRounds(self, tasks: List[int]) -> int:
        cnter = Counter(tasks)
        ans = 0 
        for num in cnter.values():
            if num == 1:
                return -1
            ans += (num + 2) // 3
        return ans

            
