class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnter = Counter()
        for w in words2:
            cnter |= Counter(w)

        ans = []
        for w in words1:
            cnter_copy = cnter.copy()
            for c in w:
                if c in cnter_copy.keys() and cnter_copy[c] > 0:
                    cnter_copy[c] -= 1
            if sum(cnter_copy.values() ) == 0:
                ans.append(w)
        return ans