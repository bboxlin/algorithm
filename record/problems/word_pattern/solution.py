class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sl = s.split()
        if len(sl) != len(pattern): return False 
        mp = {}
        bind = set() 
        for i, word in enumerate(sl):
            if pattern[i] not in mp:
                # to avoid new pattern char pair with a binded word 
                if word in bind:
                    return False
                mp[pattern[i]] = word
                bind.add(word)
            else:
                if mp[pattern[i]] != word:
                    return False 
        return True
