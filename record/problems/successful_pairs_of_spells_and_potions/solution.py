class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        potions.sort()
        ans = [0] * n
        for i in range(n):
            spell = spells[i]
            # Binary search find the left possible 
            l, r = 0, m
            while l < r:
                mid = (r + l) // 2
                if potions[mid] * spell >= success:
                    r = mid
                else:
                    l = mid + 1
            ans[i] = m - l
        return ans
        