class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        freqCnter = defaultdict(int)
        for gs in garbage:
            for g in gs:
                freqCnter[g] += 1
        ans = 0
        n = len(garbage)
        for garbageTyp in "GPM":
            for i in range(n):
                if freqCnter[garbageTyp] <= 0:
                    break
                if i > 0: ans += travel[i-1]
                gnum = garbage[i].count(garbageTyp)
                ans += gnum
                freqCnter[garbageTyp] -= gnum
        return ans