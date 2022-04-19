import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            idx = [0]*26
            for c in s:
                idx[ord(c) - ord('a')] += 1
            ans[tuple(idx)].append(s)
        return ans.values()