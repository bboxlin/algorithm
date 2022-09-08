class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        distinctSet = set()
        ans = 0
        l = 0
        for r in range(n):
            while s[r] in distinctSet:
                distinctSet.remove(s[l])
                l += 1
            distinctSet.add(s[r])
            ans = max(ans, len(distinctSet))
        return ans 