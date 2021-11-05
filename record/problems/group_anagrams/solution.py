class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for string in strs:
            key_lst = [c for c in string]
            key = str(sorted(key_lst))
            if key not in memo:
                memo[key] = [string]
            else:
                memo[key].append(string)
                
        return list(memo.values())