class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        unique = [""]
        for s in arr:
            for u in unique:
                x = s + u
                if len(x) == len(set(x)):
                    unique.append(x)
                    ans = max(ans, len(x))
        return ans