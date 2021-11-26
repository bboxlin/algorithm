class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def hash(s):
            key = []
            for c in s:
                key.append((ord(c) - ord(s[0])) % 26)
            return tuple(key)
        
        memo = collections.defaultdict(list)
        for s in strings:
            key = hash(s)
            memo[key].append(s)
            
        return memo.values()