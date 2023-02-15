class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        total = 0
        for i in range(n):
            total += 10**(n-i-1) * num[i]
        total += k
        return [int(d) for d in str(total)] 
        