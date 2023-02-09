class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        count = [set() for _ in range(26)]
        for idea in ideas:
            i = ord(idea[0]) - ord('a')
            count[i].add(idea[1:])
        res = 0
        for i in range(25):
            for j in range(i+1, 26):
                li = len(count[i])
                lj = len(count[j])
                x = len(count[i] & count[j])
                res += 2 * (li - x) * (lj - x)
        return res

